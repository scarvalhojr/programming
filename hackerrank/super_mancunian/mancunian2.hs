
import qualified Data.Maybe  as M (isNothing, catMaybes)
import qualified Data.IntSet as S (IntSet, fromList, size, member, insert,
                                   union, findMin, findMax, toList)
import qualified Data.List   as L (find, delete, deleteFirstsBy, sortOn)

type Cost = Int

type Level = Int
type LevelSet = S.IntSet
type SubPaths = [LevelSet]

data Connection = Connection Level Level Cost
  deriving Show

cost :: Connection -> Cost
cost (Connection _ _ c) = c

type OrderedConnections = [Connection]

data Path = Path { subPaths :: SubPaths
                 , totalCost :: Cost
                 , maxConnCost :: Cost }

instance Show Path where
  show (Path subpaths pcost maxcost)
    = "Path sub-paths:" ++ show (map S.toList subpaths) ++ " cost:" ++
      show pcost ++ " max cost:" ++ show maxcost

costMinPath :: Level -> OrderedConnections -> Maybe Cost
costMinPath levels conns
  | isComplete levels path  = Just (totalCost path - maxConnCost path)
  | otherwise               = Nothing
  where start = Path [] 0 0
        path  = findCostMinPath levels conns start

findCostMinPath :: Level -> OrderedConnections -> Path -> Path
findCostMinPath _      []     path = path
findCostMinPath levels (c:cs) path = findCostMinPath levels cs path'
  -- TODO: check if path is complete and stop recursing asap
  where path' = addConnection path c

addConnection :: Path -> Connection -> Path
addConnection path@(Path subpaths totcost maxcost) (Connection l1 l2 conncost)
  | M.isNothing s1 && M.isNothing s2  = Path addedset totcost' maxcost'
  | M.isNothing s1                    = Path updateds2 totcost' maxcost'
  | M.isNothing s2                    = Path updateds1 totcost' maxcost'
  | S.member l1 set2                  = path -- connection creates cycle
  | otherwise                         = Path mergedset totcost' maxcost'
  where s1        = L.find (S.member l1) subpaths
        s2        = L.find (S.member l2) subpaths
        addedset  = (S.fromList [l1, l2]) : subpaths
        Just set1 = s1
        Just set2 = s2
        updateds1 = (S.insert l2 set1) : (L.delete set1 subpaths)
        updateds2 = (S.insert l1 set2) : (L.delete set2 subpaths)
        mergedset = (S.union set1 set2) : (L.deleteFirstsBy (==) subpaths [set1, set2])
        totcost'  = totcost + conncost
        maxcost'  = max maxcost conncost

isComplete :: Level -> Path -> Bool
isComplete levels (Path subpaths _ _)
  = length subpaths == 1 && S.size levelset == levels &&
    S.findMax levelset == levels && S.findMin levelset == 1
  where levelset = head subpaths

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
