
import qualified Data.Maybe  as M (catMaybes)
import qualified Data.List   as L (nub, sortOn)
import qualified Data.IntMap as H (IntMap, empty, insert, findWithDefault, size,
                                   member, keys)

---

data DisjointIntSet = DisjointIntSet { parentMap :: H.IntMap Int
                                     , rankMap   :: H.IntMap Int }

emptyDisjointIntSet :: DisjointIntSet
emptyDisjointIntSet = DisjointIntSet H.empty H.empty

sizeSet :: DisjointIntSet -> Int
sizeSet (DisjointIntSet parentmap _) = H.size parentmap

findRoot :: DisjointIntSet -> Int -> Int
findRoot dset@(DisjointIntSet parentmap _) key
  | parent == key  = key
  | otherwise      = findRoot dset parent
  where parent = H.findWithDefault key key parentmap

joinSets :: DisjointIntSet -> Int -> Int -> Maybe DisjointIntSet
joinSets dset@(DisjointIntSet parentmap ranks) k1 k2
  | root1 == root2 = Nothing
  | rank1 < rank2  = Just (DisjointIntSet addR1toR2 ranks)
  | rank2 < rank1  = Just (DisjointIntSet addR2toR1 ranks)
  | rank1 == 0     = Just (DisjointIntSet addnewset ranks')
  | otherwise      = Just (DisjointIntSet addR2toR1 ranks')
  where root1     = findRoot dset k1
        root2     = findRoot dset k2
        rank1     = H.findWithDefault 0 root1 ranks
        rank2     = H.findWithDefault 0 root2 ranks
        addR1toR2 = H.insert root1 root2 parentmap
        addR2toR1 = H.insert root2 root1 parentmap
        addnewset = H.insert root1 root1 addR2toR1
        ranks'    = H.insert root1 (rank1 + 1) ranks

isDisjoint :: DisjointIntSet -> Bool
isDisjoint dset@(DisjointIntSet parentmap _) = length unique > 1
  where roots  = map (findRoot dset) (H.keys parentmap)
        unique = take 2 (L.nub roots)

---

type Cost = Int
type Level = Int

data Path = Path { levelSets :: DisjointIntSet
                 , totalCost :: Cost
                 , maxConnCost :: Cost }

data Connection = Connection Level Level Cost

cost :: Connection -> Cost
cost (Connection _ _ c) = c

type OrderedConnections = [Connection]

costMinPath :: Level -> OrderedConnections -> Maybe Cost
costMinPath levels conns
  | isComplete levels path  = Just (totalCost path - maxConnCost path)
  | otherwise               = Nothing
  where start = Path emptyDisjointIntSet 0 0
        path  = findCostMinPath levels conns start

findCostMinPath :: Level -> OrderedConnections -> Path -> Path
findCostMinPath _      []     path = path
findCostMinPath levels (c:cs) path = findCostMinPath levels cs path'
  -- TODO: check if path is complete and stop recursing asap
  where path' = addConnection path c

addConnection :: Path -> Connection -> Path
addConnection path@(Path levelsets totcost maxcost) (Connection l1 l2 conncost)
  = case joinSets levelsets l1 l2 of
      Nothing -> path
      Just ls -> Path ls totcost' maxcost'
  where totcost'   = totcost + conncost
        maxcost'   = max maxcost conncost

isComplete :: Level -> Path -> Bool
isComplete levels (Path levelsets _ _)
  = sizeSet levelsets == levels && not (isDisjoint levelsets)

---

main :: IO ()
main = do
    line <- getLine
    let levels = read (head (words line)) :: Int

    rest <- getContents
    let connections = M.catMaybes $ map parseConnection (lines rest)
    let orderedConnections = L.sortOn cost connections

    let minCost = costMinPath levels orderedConnections
    let cost = case minCost of
                   Nothing -> -1
                   Just c  -> c
    putStrLn $ show cost

parseConnection :: String -> Maybe Connection
parseConnection line
  | length nums /= 3  = Nothing
  | otherwise         = Just (Connection (nums!!0) (nums!!1) (nums!!2))
  where nums = map read (words line) :: [Int]
