
import qualified Data.List   as L (nub)
import qualified Data.IntMap as H (IntMap, empty, insert, findWithDefault, size,
                                   member, keys)

data DisjointIntSet = DisjointIntSet { parentMap :: H.IntMap Int
                                     , rankMap   :: H.IntMap Int }
  deriving Show

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
joinSets dset@(DisjointIntSet parentmap rankmap) k1 k2
  | root1 == root2 = Nothing
  | rank1 < rank2  = Just (DisjointIntSet map1to2 rankmap)
  | rank2 < rank1  = Just (DisjointIntSet map2to1 rankmap)
  | rank1 == 0     = Just (DisjointIntSet newset rankmap')
  | otherwise      = Just (DisjointIntSet map2to1 rankmap')
  where root1    = findRoot dset k1
        root2    = findRoot dset k2
        rank1    = H.findWithDefault 0 root1 rankmap
        rank2    = H.findWithDefault 0 root2 rankmap
        map1to2  = H.insert root1 root2 parentmap
        map2to1  = H.insert root2 root1 parentmap
        newset   = H.insert root1 root1 map2to1
        rankmap' = H.insert root1 (rank1 + 1) rankmap

isDisjoint :: DisjointIntSet -> Bool
isDisjoint dset@(DisjointIntSet parentmap _) = length unique > 1
  where roots  = map (findRoot dset) (H.keys parentmap)
        unique = take 2 (L.nub roots)
        -- TODO: count how many keys are parents of themselves
