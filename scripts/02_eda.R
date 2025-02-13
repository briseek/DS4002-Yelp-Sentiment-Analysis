df <- read.csv("FINAL_yelp_dataframe.csv", header = TRUE)


# Counts of Restaurants that are Opened and Closed
library(dplyr)
df %>%
  group_by(state)%>%
  summarise(n = n())

library(ggplot2)

ggplot(df, aes(x = factor(is_open, labels = c("Closed", "Open")))) + geom_bar(fill = "lightblue") + 
  labs(x = "Restaurant Status",y = "Count",
     title = "Distribution of Open and Closed Restaurants in Philadelphia") +
  theme_light() + scale_y_continuous(breaks = seq(0, 15000, 1000))

# Distribution of Star Rating
graph1 <- ggplot(df, aes(x=stars, fill = factor(is_open, labels = c("Closed", "Open"))))+
  geom_histogram(aes(y = ..density..), binwidth = 0.5, alpha = 0.75) + 
  geom_density(color = "black", bw = 0.25, fill = "transparent") +
  facet_wrap(~factor(is_open, labels = c("Closed", "Open"))) + theme(legend.position = "none") + labs(x = "Average Star Rating", y = "Density", title = "Distribution of Average Star Rating by Restaurant Status for Philadelphia")

graph2 <- ggplot(df, aes(x=stars, fill = factor(is_open, labels = c("Closed", "Open"))))+
  geom_histogram(binwidth = 0.5, alpha = 0.75) + 
  facet_wrap(~factor(is_open, labels = c("Closed", "Open"))) + theme(legend.position = "none") + labs(x = "Average Star Rating", y = "Counts", title = "Histogram of Average Star Rating by Restaurant Status for Philadelphia")

library(patchwork)
combined_plot <- graph1 + graph2 + plot_layout(ncol = 1, nrow = 2)

combined_plot                                                                 

# Distribution of Average Compound Score
ggplot(df, aes(x =  compound, fill = factor(is_open, labels = c("Closed", "Open")))) + 
  geom_density() + 
  scale_fill_manual(values = c("Closed" = "indianred", "Open" = "cadetblue")) + 
  labs(x = "Restaurant Status", y = "Density") +
  theme(legend.position = "none") + facet_wrap(~factor(is_open, labels = c("Closed", "Open"))) + labs(x = "Average Compound Sentiment Score", y = "Density", title = "Distribution of Average Compound Score by Restuarant Status for Philadelphia")
