
main :: IO ()
main = do
    line <- getLine
    let numbers = map read (words line) :: [Int]
    putStrLn $ show (maximum numbers)
