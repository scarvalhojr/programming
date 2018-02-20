
import qualified Data.List                  as L (unfoldr)
import qualified Data.ByteString.Lazy.Char8 as B (ByteString, getContents,
                                                  readInt, drop)

main :: IO ()
main = do
    line <- B.getContents
    let numbers = parse line
    putStrLn $ show (maximum numbers)

parse :: B.ByteString -> [Int]
parse = L.unfoldr step
  where step bs = case B.readInt bs of
                    Nothing     -> Nothing
                    Just (k, t) -> Just (k, B.drop 1 t)
