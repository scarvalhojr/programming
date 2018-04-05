
import qualified Data.List as L (unfoldr, sort)
import qualified Data.ByteString.Lazy.Char8 as B (ByteString, getContents,
                                                  readInteger, drop)

main :: IO ()
main = do
  _ <- getLine
  rest <- B.getContents
  let numbers = parseInts rest
  mapM_ print (L.sort numbers)

parseInts :: B.ByteString -> [Integer]
parseInts = L.unfoldr step
  where step bs = case B.readInteger bs of
                    Nothing     -> Nothing
                    Just (k, t) -> Just (k, B.drop 1 t)
