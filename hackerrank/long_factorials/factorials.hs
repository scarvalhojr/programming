import System.IO

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Integer
    print $ product [1..n]
