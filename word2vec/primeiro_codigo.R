# Inicializando o cluster H2O
library(dplyr)
library(h2o)

h2o.init()

# Importando a base de dados
job.title.path <- "https://raw.githubusercontent.com/h2oai/sparkling-water/rel-1.6/examples/smalldata/craigslistJobTitles.csv"
job.titles <- h2o.importFile(job.title.path, 
                             destination_frame = "jobtitles",
                             col.names = c("category", "jobtitle"),
                             col.types = c("Enum", "String"),
                             header = TRUE)

# Tranformando os dados em dataFrame
job.titles_r <- as.data.frame(job.titles)
job.titles_r %>% View() 
table(job.titles_r$category)


# Tratando o texto
library(tm)
STOP_WORDS <- stopwords(kind = 'en')

tokenize <- function(sentences, stop.words = STOP_WORDS) {
  # Separa as palavras
  tokenized <- h2o.tokenize(sentences, "\\\\W+")
  
  # Converte para minúsculo
  tokenized.lower <- h2o.tolower(tokenized)
  
  # Remove palavras com menos de 2 caracteres
  tokenized.lengths <- h2o.nchar(tokenized.lower)
  tokenized.filtered <- tokenized.lower[is.na(tokenized.lengths) || tokenized.lengths >= 2,]
  
  # Remove palavras que contém números
  tokenized.words <- tokenized.filtered[h2o.grep("[0-9]", tokenized.filtered, invert = TRUE, output.logical = TRUE),]
  
  # Remove stop words
  tokenized.words <- tokenized.words[is.na(tokenized.words) || (!tokenized.words %in% STOP_WORDS),]

  return(tokenized.words)  
}

palavras <- tokenize(job.titles$jobtitle)

## Construção do modelo word2vec
