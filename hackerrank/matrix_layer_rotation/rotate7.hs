-- A more readable version of
-- https://www.hackerrank.com/rest/contests/master/challenges/matrix-rotation-algo/hackers/d_n_s/download_solution

main :: IO ()
main = do
    [nrows, ncols, rotation] <- map (read :: String -> Int) . words <$> getLine
    matrix <- map (map (read :: String -> Int) . words) . lines <$> getContents
    mapM_ putStrLn $ map unwords $ map (map show) (
        rotateMatrix matrix nrows ncols rotation)

rotateMatrix :: [[a]] -> Int -> Int -> Int -> [[a]]
rotateMatrix matrix _ _ 0 = matrix
rotateMatrix matrix nrows ncols rotation =
    [[matrix!!rot_row!!rot_col |
        (rot_row, rot_col) <- [rotateCoord nrows ncols row col rotation |
            col <- [0..ncols - 1]]] | row <- [0..nrows - 1]]

rotateCoord :: Int -> Int -> Int -> Int -> Int -> (Int, Int)
rotateCoord nrows ncols row col rotation =
    rotateCoord' (nrows - 1) (ncols - 1) row col rotation 0

rotateCoord' :: Int -> Int -> Int -> Int -> Int -> Int -> (Int, Int)
rotateCoord' maxrow maxcol row col rotation layer
    | row == 0       = rotateIdx (col)
    | col == maxcol  = rotateIdx (col + row)
    | row == maxrow  = rotateIdx (2 * maxcol + maxrow - col)
    | col == 0       = rotateIdx (2 * maxcol + 2 * maxrow - row)
    | otherwise      = rotateCoord' (maxrow - 2) (maxcol - 2) (row - 1)
                                    (col - 1) rotation (layer + 1)
    where rotateIdx  = rotateIndex maxrow maxcol rotation layer

rotateIndex :: Int -> Int -> Int -> Int -> Int -> (Int, Int)
rotateIndex maxrow maxcol rotation layer index =
    coordFromIndex maxrow maxcol layer rotated_index
    where layer_length = 2 * (maxcol + maxrow)
          rotated_index = (index + rotation) `mod` layer_length

coordFromIndex :: Int -> Int -> Int -> Int -> (Int, Int)
coordFromIndex maxrow maxcol layer index =
    (layer + inner_row, layer + inner_col)
    where (inner_row, inner_col)
            | index <= maxcol               = (0, index)
            | index <= maxcol + maxrow      = (index - maxcol, maxcol)
            | index <= 2 * maxcol + maxrow  = (maxrow, 2 * maxcol + maxrow - index)
            | otherwise                     = (2 * maxcol + 2 * maxrow - index, 0)
