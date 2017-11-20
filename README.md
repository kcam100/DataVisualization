
<center>
# Udacity P6 - Titanic Data Visualization
***

**By:** Kyle Campbell <br>
**Date:** October 15, 2017

<center>
# Summary
***

The Titanic dataset features records from 891 out of the 2224 passengers and crew that were aboard the Titanic during it's tragic voyage in 1912. Additional cleaning of the dataset was done in Python, including removing unnecessary columns and calculating survival rates which were then put into a new list and exported to ```.csv``` format. I decided to focus on creating a data visualization that showcases survival rates based on the sex and socioeconomic status of passengers aboard the Titanic.

<center>
# Design
***

## **INITIAL SKETCH:**
<img src='http://preview.ibb.co/dT2T0m/sketch1.jpg', width=500px, height=400px, align=center>
<br>
The sketch (above) is my first interpretation of how I thought to present the data from the Titanic dataset. I knew that I wanted my chart to be a grouped bar chart since I wanted to represent survival rates on the y-axis with a few different categorical variables along the x-axis. Initially, I wanted to showcase survival rate with three different variables (sex, socioeconomic class, and age), however after receiving feedback from my initial sketch that it was too much information, I decided to focus on sex and socioeconomic class. 
***
## **FIRST CODED VISUALIZATION:**
<img src='http://image.ibb.co/cqyCRR/Titanic_Visualization1.png', width=500px, height=400px, align=center>
<br>
The visualization above is my first coded example (```index1.html```). I used ```dimple.js``` to build my grouped bar chart. I decided to use the built in tooltip animation so that the values and variables could be seen while hovering over each bar. After receiving feedback, I noticed a number of small problems that needed adjusted. I forgot to put a legend to indicate sex (male/female colors). In addition, one of my reviewers suggested that I switch the colors due to a lot of people subconsciously associating pink with females and blue with males. I also needed a more descriptive title (variables explained, passengers, etc). It was also noted that 'value' as the y-axis label was too vague, and I needed to format the y-tick to show 2 decimal places for a more accurate representation of the data.
***
## **FINAL VISUALIZATION:**
<img src='http://image.ibb.co/ghDOY6/Titanic_Visualization_FINAL.png', width=500px, height=400px, align=center>
<br>
My final visualization (```indexFINAL.html```), shown above, accurately reflects the message that I wanted to convey. The final visualization shows the relationship between sex, socioeconomic class and survival rate. It can be easily inferred that females had a higher survival rate than their male counterparts. In addition, it's easy to see how first class passengers had a much higher survival rate than the lower class passengers.
<br><br>
The following items were corrected to produce the final Titanic visualization: y-axis label changed from 'value' to 'Survival Rate' by updating the column name in ```titanic_survival_rates2.csv```, y-tick format updated to show hundredths value, more descriptive title, centered graph/text on page, legend indicating variable represented by color, underline added to title, switched to a pinkish color for female and blueish color for male.


<center>
# Feedback
***

## #1 
> "I notice that the females have a higher survival. How many people are in the data? First class women have the highest survival rate. Should put a more descriptive title, as well as a better y-axis label."

## #2
> "Title not properly labeled. What is class? Strong relationship between gender and survival. Rich people were better off than poor people. Graph needs centered(was left aligned in 1st iteration). Y-axis value should go to hundredths."

## #3
> "Higher proportion of women survived than men. Upper class were more likely to survive also. Poor people got the short end of the stick. Male and female colors are confusing (after 1st iteration male was pinkish, female was blueish). Needs a legend to explain."


<center>
# Resources
***

+ Udacity Data Visualization course
+ https://www.digitalocean.com/community/tutorials/how-to-make-a-bar-chart-with-javascript-and-the-d3-library
+ https://bl.ocks.org/mbostock/3019563
+ https://www.dashingd3js.com/lessons/basic-chart-grouped-bar-chart
+ http://bl.ocks.org/juan-cb/ac731adaeadd3e855d26
+ https://gist.github.com/mbostock/3887051
+ https://blog.graphiq.com/finding-the-right-color-palettes-for-data-visualizations-fcd4e707a283
+ http://dimplejs.org/examples_viewer.html?id=bars_vertical_grouped
+ http://www.color-hex.com/color-palette/18969
