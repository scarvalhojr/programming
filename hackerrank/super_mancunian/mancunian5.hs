
import qualified Data.List   as L (sortOn)
import qualified Data.Maybe  as M (catMaybes, isNothing, fromJust)
import qualified Data.IntMap as H (IntMap, empty, insert, findWithDefault,
                                   toList)

---

data DisjointIntSet = DisjointIntSet { numElems :: Int
                                     , parentMap  :: H.IntMap Int
                                     , rankMap    :: H.IntMap Int }

emptyDisjointIntSet :: DisjointIntSet
emptyDisjointIntSet = DisjointIntSet 0 H.empty H.empty

findRoot :: DisjointIntSet -> Int -> Int
findRoot dset@(DisjointIntSet _ parents _) key
  | parent == key  = key
  | otherwise      = findRoot dset parent
  where parent = H.findWithDefault key key parents

joinSets :: DisjointIntSet -> Int -> Int -> Maybe DisjointIntSet
joinSets dset@(DisjointIntSet num parents ranks) k1 k2
  | root1 == root2            = Nothing
  | rank1 == 0 && rank2 == 0  = Just (DisjointIntSet (num + 2) newset ranks')
  | rank1 == 0                = Just (DisjointIntSet (num + 1) add1to2 ranks)
  | rank2 == 0                = Just (DisjointIntSet (num + 1) add2to1 ranks)
  | rank1 < rank2             = Just (DisjointIntSet num add1to2 ranks)
  | rank2 < rank1             = Just (DisjointIntSet num add2to1 ranks)
  | otherwise                 = Just (DisjointIntSet num add2to1 ranks')
  where root1   = findRoot dset k1
        root2   = findRoot dset k2
        rank1   = H.findWithDefault 0 root1 ranks
        rank2   = H.findWithDefault 0 root2 ranks
        add1to2 = H.insert root1 root2 parents
        add2to1 = H.insert root2 root1 parents
        newset  = H.insert root1 root1 add2to1
        ranks'  = H.insert root1 (rank1 + 1) ranks

isDisjoint :: DisjointIntSet -> Bool
isDisjoint (DisjointIntSet _ parentmap _) = length roots > 1
  where roots = take 2 $ filter (uncurry (==)) (H.toList parentmap)

---

type Cost = Int
type Level = Int
type LevelSets = DisjointIntSet

data Path = Path { levelSets         :: LevelSets
                 , totalCost         :: Cost
                 , maxConnCost       :: Cost
                 , maxConnCount      :: Int
                 , preMagicLevelSets :: LevelSets }

data Connection = Connection Level Level Cost

cost :: Connection -> Cost
cost (Connection _ _ c) = c

magicPaths :: Level -> [Connection] -> Maybe (Cost, Int)
magicPaths numlevels connections
  | M.isNothing maybepath  = Nothing
  | otherwise              = Just (magiccost, magiccount)
  where start       = Path emptyDisjointIntSet 0 0 0 emptyDisjointIntSet
        sortedconns = L.sortOn cost connections
        maybepath   = findMinPath numlevels sortedconns start
        finalpath   = M.fromJust maybepath
        maxcost     = maxConnCost finalpath
        magiccost   = totalCost finalpath - maxcost
        magicconns  = dropWhile ((< maxcost) . cost) sortedconns
        magiclevels = preMagicLevelSets finalpath
        magiccount  = length $ filter (connectLevels magiclevels) magicconns

findMinPath :: Level -> [Connection] -> Path -> Maybe Path
findMinPath _ [] _ = Nothing
findMinPath numlevels (c:cs) path
  | M.isNothing maybepath        = findMinPath numlevels cs path
  | isComplete numlevels levels  = maybepath
  | otherwise                    = findMinPath numlevels cs path'
  where maybepath = addConnection c path
        path'     = M.fromJust maybepath
        levels    = levelSets path'

addConnection :: Connection -> Path -> Maybe Path
addConnection (Connection l1 l2 ccost) (Path levels tcost mcost mcount plevels)
  | M.isNothing mlevels  = Nothing
  | ccost > mcost        = Just (Path levels' tcost' ccost 1 levels)
  | otherwise            = Just (Path levels' tcost' mcost (mcount + 1) plevels)
  where mlevels = joinSets levels l1 l2
        levels' = M.fromJust mlevels
        tcost'  = tcost + ccost

isComplete :: Level -> LevelSets -> Bool
isComplete numlevels set = numElems set == numlevels && not (isDisjoint set)

connectLevels :: LevelSets -> Connection -> Bool
connectLevels sets (Connection l1 l2 _) = findRoot sets l1 /= findRoot sets l2

---

main :: IO ()
main = do
    line <- getLine
    let numlevels = read (head (words line)) :: Int

    rest <- getContents
    let connections = M.catMaybes $ map parseConnection (lines rest)

    let (cost, count) = case magicPaths numlevels connections of
                          Nothing     -> (-1, -1)
                          Just (c, n) -> (c, n)
    putStrLn $ show cost ++ " " ++ show count

parseConnection :: String -> Maybe Connection
parseConnection line
  | length nums /= 3  = Nothing
  | otherwise         = Just (Connection (nums!!0) (nums!!1) (nums!!2))
  where nums = map read (words line) :: [Int]
