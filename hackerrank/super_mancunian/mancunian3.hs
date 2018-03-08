
import qualified Data.Maybe  as M (catMaybes)
import qualified Data.List   as L (nub, sortOn)
import qualified Data.IntMap as H (IntMap, empty, insert, findWithDefault, size,
                                   member, keys)

---

data DisjointIntSet = DisjointIntSet (H.IntMap Int)

emptyDisjointIntSet :: DisjointIntSet
emptyDisjointIntSet = DisjointIntSet H.empty

sizeSet :: DisjointIntSet -> Int
sizeSet (DisjointIntSet parentmap) = H.size parentmap

findRoot :: DisjointIntSet -> Int -> Int
findRoot dset@(DisjointIntSet parentmap) key
  | parent == key  = key
  | otherwise      = findRoot dset parent
  where parent = H.findWithDefault key key parentmap

joinSets :: DisjointIntSet -> Int -> Int -> DisjointIntSet
joinSets (DisjointIntSet parentmap) k1 k2
  | H.member k1 parentmap  = DisjointIntSet (H.insert k2 k1 parentmap)
  | otherwise              = DisjointIntSet (H.insert k2 k1 parentmap')
  where parentmap' = H.insert k1 k1 parentmap

isDisjoint :: DisjointIntSet -> Bool
isDisjoint dset@(DisjointIntSet parentmap) = length unique > 1
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
  | root1 == root2    = path
  | otherwise         = Path levelsets' totcost' maxcost'
  where root1      = findRoot levelsets l1
        root2      = findRoot levelsets l2
        levelsets' = joinSets levelsets root1 root2
        totcost'   = totcost + conncost
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
