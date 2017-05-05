-- Convert matrix (row, col) matrix coordinates to a (layer, index) pair
-- by recursively probing the limits of every inner layer, rotate index,
-- and convert it back to (row, col).

main :: IO ()
main = do
    [nrows, ncols, rotation] <- map (read :: String -> Int) . words <$> getLine
    matrix <- map (map (read :: String -> Int) . words) . lines <$> getContents
    let result = rotateMatrix matrix nrows ncols rotation
    mapM_ putStrLn $ map unwords $ map (map show) result


rotateMatrix :: [[a]] -> Int -> Int -> Int -> [[a]]
rotateMatrix matrix _ _ 0 = matrix
rotateMatrix matrix nrows ncols rotation =
    [[matrix!!rot_row!!rot_col |
        (rot_row, rot_col) <- [rotateCoord nrows ncols row col rotation |
            col <- [0..ncols - 1]]] | row <- [0..nrows - 1]]

rotateCoord :: Int -> Int -> Int -> Int -> Int -> (Int, Int)
rotateCoord nrows ncols row col rotation
    | rotated_idx == idx  = (row, col)
    | otherwise           = getRowCol nrows ncols layer rotated_idx
    where (layer, idx) = getLayerIndex nrows ncols row col
          layer_length = 2 * (nrows + ncols - 4 * layer - 2)
          rotated_idx  = (idx + rotation) `mod` layer_length

getLayerIndex :: Int -> Int -> Int -> Int -> (Int, Int)
getLayerIndex nrows ncols row col =
    getLayerIndex' (nrows - 1) (ncols - 1) row col 0

getLayerIndex' :: Int -> Int -> Int -> Int -> Int -> (Int, Int)
getLayerIndex' maxrow maxcol row col layer
    | row == 0       = (layer, col)
    | col == maxcol  = (layer, col + row)
    | row == maxrow  = (layer, 2 * maxcol + maxrow - col)
    | col == 0       = (layer, 2 * maxcol + 2 * maxrow - row)
    | otherwise      = getLayerIndex' (maxrow - 2) (maxcol - 2) (row - 1)
                                      (col - 1) (layer + 1)

getRowCol :: Int -> Int -> Int -> Int -> (Int, Int)
getRowCol nrows ncols layer index = (layer + row, layer + col)
    where width  = ncols - 2 * layer - 1
          height = nrows - 2 * layer - 1
          (row, col)
            | index <= width              = (0, index)
            | index <= width + height     = (index - width, width)
            | index <= 2 * width + height = (height, 2 * width + height - index)
            | otherwise                   = (2 * width + 2 * height - index, 0)
