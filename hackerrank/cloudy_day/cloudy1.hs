
import Data.List (partition, delete)


data Town = Town { townPos :: Int, population :: Int }
  deriving Show

data Cloud = Cloud { cloudPos :: Int, range :: Int }
  deriving (Show, Eq)


main :: IO ()
main = do
    -- ignore first line of input (number of towns)
    _ <- getLine

    p <- getLine
    let populations = map read (words p) :: [Int]
    x <- getLine
    let townPositions = map read (words x) :: [Int]
    let towns = map (uncurry Town) (zip townPositions populations)

    -- ignore next line of input (number of clouds)
    _ <- getLine

    y <- getLine
    let cloudPositions = map read (words y) :: [Int]
    r <- getLine
    let ranges = map read (words r) :: [Int]
    let clouds = map (uncurry Cloud) (zip cloudPositions ranges)

    putStrLn $ show (maxSunnyPopulation clouds towns)


maxSunnyPopulation :: [Cloud] -> [Town] -> Int
maxSunnyPopulation clouds towns = sumPopulation sunnyTowns + maximum reliefs
  where (sunnyTowns, cloudyTowns) = partition (isSunny clouds) towns
        reliefs = map (relief clouds cloudyTowns) clouds

covers :: Town -> Cloud -> Bool
covers (Town tp _) (Cloud cp r) = (cp - r <= tp) && (tp <= cp + r)

isSunny :: [Cloud] -> Town -> Bool
isSunny clouds town = all (not . covers town) clouds

sumPopulation :: [Town] -> Int
sumPopulation = sum . map population

relief :: [Cloud] -> [Town] -> Cloud -> Int
relief clouds towns c = sumPopulation sunnyTowns
  where otherClouds = delete c clouds
        sunnyTowns  = filter (isSunny otherClouds) towns
