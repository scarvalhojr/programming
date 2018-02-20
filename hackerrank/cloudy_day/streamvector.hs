
import qualified Data.Vector                as V (Vector, unfoldr, maximum)
import qualified Data.ByteString.Lazy.Char8 as B (ByteString, getContents,
                                                  readInt, drop)

main :: IO ()
main = do
    line <- B.getContents
    let numbers = parse line
    putStrLn $ show (V.maximum numbers)

parse :: B.ByteString -> V.Vector Int
parse = V.unfoldr step
  where step bs = case B.readInt bs of
                    Nothing     -> Nothing
                    Just (k, t) -> Just (k, B.drop 1 t)
