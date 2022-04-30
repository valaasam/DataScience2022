library(readr)
library(reshape2)
library(lme4)
library(ggplot2)
library(car)
library(ggpubr)
library(plotrix)


############################.
####  Read in/Organize  ####
############################.

setwd("/Users/val/Desktop/testrun")

####  Read in Data  ####

#should be file from May2020, after Yong changed standardization to be based on highest value
data<-read_csv("combined_cleaned.csv")

library(dplyr)
condensed <- data %>% 
  group_by(cage, hour, date) %>% 
  summarise(totalhops=sum(hops))  %>% 
  group_by(cage, hour) %>%
  summarise(sd=sd(totalhops), n=n(), se=sd/sqrt(n), mean=mean(totalhops))

cage1<-subset(condensed, cage=="1")

plot1 <-
  ggplot(cage1, aes(x=hour, y=mean))+
 # geom_line(data=cage1, linetype=1, size=.5, aes(x=hour, y=mean)) +
  geom_point(data=cage1, shape=16, size=2, aes(x=hour, y=mean)) +
  geom_smooth(data=cage1, aes(ymin=(mean-se), ymax=(mean+se)), size=.2, fill="royalblue1", color="black") +
  scale_color_manual(values ="royalblue1", labels="") +
  xlab("Hours (ZT)")+
  ylab("Activity (average hops)") +
  theme_classic() +
  theme(
    axis.title.x = element_text(size=14, family="Times"),
    axis.text.x  = element_text(size=12, family="Times", color = "black"),
    axis.title.y = element_text(size=14, family="Times"),
    axis.text.y  = element_text(size=12, family="Times", color = "black"),
    legend.title = element_blank(),
    legend.text = element_text(size = 12, family="Times"),
    plot.title = element_blank()
  )

plot1
plot1.lims<-get_plot_limits(plot1)[3:4]




#####################.
####  ANALYSIS   ####
#####################.
library(cosinor2)
library(cosinor)
cosinedat <-
  data %>% 
  group_by(cage, hour, date) %>% 
  summarise(totalhops=sum(hops))
cosinedat <-as.data.frame(subset(cosinedat, cage=="1"))


fit <- cosinor.lm(totalhops ~ time(hour), period = 24, data = cosinedat)
summary(fit)
cosinor.detect(fit)
cosinor.PR(fit)

#determining effect of treatment on groups
cosinor.lm(Y ~ time(time) + treat + amp.acro(treat), data = data)
test_cosinor(fit, "treat", param = "amp")   
test_cosinor(fit, "treat", param = "acr")   