
import qualified Data.Set   as S (Set, empty, singleton, fromList, delete, size,
                                  member, unions, toList)
import qualified Data.List  as L (delete, find, sortOn)
import qualified Data.Maybe as M (isNothing, isJust, catMaybes)

type Level = Int
type Cost = Int

data Connection = Connection Level Level Cost
  deriving (Eq, Ord, Show) -- TODO: implement Eq comparing levels only

cost :: Connection -> Cost
cost (Connection _ _ c) = c

maxBy :: Ord a => (b -> a) -> b -> b -> b
maxBy f x1 x2 = if compare (f x1) (f x2) >= EQ then x1 else x2

maybeSingleton :: Maybe a -> S.Set a
maybeSingleton Nothing  = S.empty
maybeSingleton (Just x) = S.singleton x

type LevelSet = S.Set Level
type OrderedConnections = [Connection]

data Path = Path { unvisitedLevels :: LevelSet
                 , remainingConnections :: OrderedConnections
                 , totalCost :: Cost
                 , magicConnection :: Maybe Connection }

instance Show Path where
  show (Path unvisited connections pcost magicConn)
    = "Path unvisited:" ++ show (S.toList unvisited) ++ " connections:" ++
      show connections ++ " cost:" ++ show pcost ++ " magic:" ++ show magicConn

createStartPath :: Level -> OrderedConnections -> Path
createStartPath levels connections = Path unvisited conns 0 Nothing
  where unvisited = S.fromList [2..levels]
        conns     = filter (inRange levels) connections

inRange :: Level -> Connection -> Bool
inRange maxlevel (Connection l1 l2 _)
  = l1 <= maxlevel && l2 <= maxlevel && l1 >= 1 && l2 >= 1

costMinPath :: Level -> OrderedConnections -> Maybe Cost
costMinPath levels conns = findCostMinPath start
  where start = createStartPath levels conns

findCostMinPath :: Path -> Maybe Cost
findCostMinPath path@(Path unvisited conns pathCost magicConn)
  | null unvisited         = Just (pathCost - magicCost)
  | M.isNothing nextConn   = Nothing
  | otherwise              = findCostMinPath path'
  where magicCost  = maybe 0 cost magicConn
        nextConn   = L.find (connects unvisited) conns
        Just conn  = nextConn
        path'      = extend path conn (maxBy (fmap cost) magicConn nextConn)

connects :: LevelSet -> Connection -> Bool
connects levels (Connection l1 l2 _) = S.member l1 levels /= S.member l2 levels

extend :: Path -> Connection -> Maybe Connection -> Path
extend (Path unvisited conns pcost _) conn = Path unvisited' conns' pcost'
  where level      = nextLevel conn unvisited
        unvisited' = S.delete level unvisited
        conns'     = L.delete conn conns
        pcost'     = pcost + cost conn

nextLevel :: Connection -> LevelSet -> Level
nextLevel (Connection l1 l2 _) levels = if S.member l1 levels then l1 else l2

countMagicConnections :: Cost -> Level -> OrderedConnections -> Int
countMagicConnections maxCost levels conns = count
  where start = createStartPath levels conns
        count = S.size (findMagicConnections maxCost start)

findMagicConnections :: Cost -> Path -> S.Set Connection
findMagicConnections maxCost path@(Path unvisited conns pcost mconn)
  | null unvisited    = maybeSingleton mconn
  | M.isJust mconn    = S.unions $ map (findMagicConnections maxCost) nextPathsNoMagic
  | otherwise         = S.unions $ map (findMagicConnections maxCost) (nextPathsNoMagic ++ nextPathsWithMagic)
  where nextConns          = filter (connects unvisited) conns
        maxConnCost        = maxCost - pcost + (maybe 0 cost mconn)
        nextConnsNoMagic   = takeWhile ((<= maxConnCost) . cost) nextConns
        nextPathsWithMagic = map (extendWithMagic True path) nextConns
        nextPathsNoMagic   = map (extendWithMagic False path) nextConnsNoMagic

extendWithMagic :: Bool -> Path -> Connection -> Path
extendWithMagic magic path conn = (extend path conn) magicConn
  where magicConn = if magic then Just conn else magicConnection path

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
    let count = countMagicConnections cost levels orderedConnections
    putStrLn $ show cost ++ " " ++ show count

parseConnection :: String -> Maybe Connection
parseConnection line
  | length nums /= 3  = Nothing
  | otherwise         = Just (Connection (nums!!0) (nums!!1) (nums!!2))
  where nums = map read (words line) :: [Int]
