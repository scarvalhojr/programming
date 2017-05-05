-- Convert matrix into an array of layers, rotate them, and convert it back to
-- a matrix.

main :: IO ()
main = do
    [_, _, rotation] <- map (read :: String -> Int) . words <$> getLine
    matrix <- map (map (read :: String -> Int) . words) . lines <$> getContents
    mapM_ (putStrLn . unwords) $ map (map show) (rotateMatrix matrix rotation)

rotateMatrix :: [[a]] -> Int -> [[a]]
rotateMatrix [] _ = []
rotateMatrix matrix 0 = matrix
rotateMatrix matrix n
    | nrows < 2             = matrix
    | ncols < 2             = matrix
    | min_dim `mod` 2 /= 0  = matrix
    | otherwise             =
        buildMatrix (rotateLayers (getLayers matrix nrows ncols) n) nrows ncols
    where nrows = length matrix
          ncols = length $ matrix!!0
          min_dim = min nrows ncols

getLayers :: [[a]] -> Int -> Int -> [[a]]
getLayers matrix nrows ncols =
    [getLayer matrix nrows ncols n | n <- [0..num_layers - 1]]
    where num_layers = min nrows ncols `div` 2

getLayer :: [[a]] -> Int -> Int -> Int -> [a]
getLayer matrix nrows ncols layer =
    [matrix!!row!!col | (row, col) <- top ++ right ++ bottom ++ left]
    where start_row = layer
          start_col = layer
          end_row = nrows - layer - 1
          end_col = ncols - layer - 1
          top = [(start_row, c) | c <- [start_col..end_col - 1]]
          right = [(r, end_col) | r <- [start_row..end_row - 1]]
          bottom = [(end_row, c) | c <- reverse [start_col + 1..end_col]]
          left = [(r, start_col) | r <- reverse [start_row + 1..end_row]]

rotateLayers :: [[a]] -> Int -> [[a]]
rotateLayers [] _ = []
rotateLayers xs 0 = xs
rotateLayers (x:xs) n = rotate x n : rotateLayers xs n

rotate :: [a] -> Int -> [a]
rotate [] _ = []
rotate xs n
    | shift == 0    = xs
    | otherwise     = take len (drop shift (cycle xs))
    where len = length xs
          shift = n `mod` len

buildMatrix :: [[a]] -> Int -> Int -> [[a]]
buildMatrix layers nrows ncols =
    [[layers!!layer!!idx | (layer, idx) <- [layerIndex nrows ncols row col |
        col <- [0..ncols - 1]]] | row <- [0..nrows - 1]]

layerIndex :: Int -> Int -> Int -> Int -> (Int, Int)
layerIndex nrows ncols row col
    | area == top     = (layer, col - layer)
    | area == right   = (layer, ncols - 3 * layer + row - 1)
    | area == bottom  = (layer, 2 * ncols + nrows - 5 * layer - col - 3)
    | area == left    = (layer, 2 * ncols + 2 * nrows - 7 * col - row - 4)
    where top    = 0
          right  = 1
          bottom = 2
          left   = 3
          in_top_half  = row < nrows `div` 2
          in_left_half = col < ncols `div` 2
          area
            | in_top_half && in_left_half && col < row  = left
            | in_top_half && col >= ncols - row         = right
            | in_top_half                               = top
            | in_left_half && col < nrows - row - 1     = left
            | col > ncols - nrows + row                 = right
            | otherwise                                 = bottom
          layer
            | area == top     = row
            | area == right   = ncols - col - 1
            | area == bottom  = nrows - row - 1
            | area == left    = col
