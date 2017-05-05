-- Instead of explicitly building the layers, manipulate matrix coordinates
-- (row, col) only.

main :: IO ()
main = do
    [rows, cols, rotation] <- map (read :: String -> Int) . words <$> getLine
    matrix <- map (map (read :: String -> Int) . words) . lines <$> getContents
    mapM_ (putStrLn . unwords) $ map (map show) (
        rotateMatrix matrix rows cols rotation)

rotateMatrix :: [[a]] -> Int -> Int -> Int -> [[a]]
rotateMatrix matrix _ _ 0 = matrix
rotateMatrix matrix nrows ncols rotation
    | nrows < 2 || ncols < 2 || (min nrows ncols) `mod` 2 /= 0  = matrix
    | otherwise =
        [[matrix!!rot_row!!rot_col |
            (rot_row, rot_col) <- [rotateCoord nrows ncols row col rotation |
                col <- [0..ncols - 1]]] | row <- [0..nrows - 1]]

rotateCoord :: Int -> Int -> Int -> Int -> Int -> (Int, Int)
rotateCoord nrows ncols row col rotation
    | rot_idx == idx   = (row, col)
    | otherwise        = getRowCol nrows ncols layer rot_idx
    where (layer, idx) = getLayerIndex nrows ncols row col
          layer_length = 2 * (nrows + ncols - 4 * layer - 2)
          rot_idx = (idx + rotation) `mod` layer_length

getLayerIndex :: Int -> Int -> Int -> Int -> (Int, Int)
getLayerIndex nrows ncols row col = (layer, index)
    where in_top_half  = row < nrows `div` 2
          in_left_half = col < ncols `div` 2
          area
            | in_top_half && in_left_half && col < row  = 'L' -- left
            | in_top_half && col >= ncols - row         = 'R' -- right
            | in_top_half                               = 'T' -- top
            | in_left_half && col < nrows - row - 1     = 'L' -- left
            | col > ncols - nrows + row                 = 'R' -- right
            | otherwise                                 = 'B' -- bottom
          layer
            | area == 'T'  = row
            | area == 'R'  = ncols - col - 1
            | area == 'B'  = nrows - row - 1
            | area == 'L'  = col
          index
            | area == 'T'  = col - layer
            | area == 'R'  = ncols - 3 * layer + row - 1
            | area == 'B'  = 2 * ncols + nrows - 5 * layer - col - 3
            | area == 'L'  = 2 * ncols + 2 * nrows - 7 * col - row - 4

getRowCol :: Int -> Int -> Int -> Int -> (Int, Int)
getRowCol nrows ncols layer index =
    (layer + row, layer + col)
    where width  = ncols - 2 * layer - 1
          height = nrows - 2 * layer - 1
          (row, col)
            | index <= width              = (0, index)
            | index <= width + height     = (index - width, width)
            | index <= 2 * width + height = (height, 2 * width + height - index)
            | otherwise                   = (2 * width + 2 * height - index, 0)
