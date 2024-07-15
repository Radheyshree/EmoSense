# Emosense: Unlocking Actionable Insights from Sentiment Analysis
============================================================

As the lead and member of the Google Developer Student Club (GDSC) at my college, I recognized the importance of understanding student feedback to create more engaging and successful events. With a large amount of unstructured data from event feedback forms, social media, and online surveys, it's challenging to extract valuable insights to improve future events. This is where Emosense comes in - a sentiment analysis API that not only analyzes student feedback but also provides actionable insights to inform business decisions.

## The Game-Changer: Top Tags for Business Decisions

What sets Emosense apart is its ability to go beyond sentiment analysis and provide a list of top tags (words) associated with each sentiment category (positive, negative, and neutral). These tags can be used to identify areas of improvement, inform marketing strategies, and drive business decisions. For instance, if the top negative tags for an event are related to food quality, the organizers can take concrete steps to improve the catering services for future events.

## Key Features

* **Sentiment Analysis**: Performs sentiment analysis on event feedback using the VADER library
* **Feedback Processing**: Processes event feedback by splitting it into individual lines, tokenizing each line, removing stopwords, and performing sentiment analysis
* **Top Tags Identification**: Identifies the top words associated with each sentiment category, providing actionable insights for business decisions
* **API Response**: Prepares a JSON response with various insights, including the cumulative sentiment, number of positive, negative, and neutral lines, and the top 10 words for each sentiment category

## Methodology

* Implemented feedback processing and sentiment analysis logic using the VADER library and custom improvisations
* Integrated VADER with Flask to create a RESTful API
* Performed word frequency analysis to identify the most common words in each sentiment category
* Calculated the cumulative sentiment by comparing the number of positive and negative lines

## Real-Life Problem-Solving Examples

* **TechFest 2023**: Analyze feedback data from last year's attendees to identify areas of improvement for TechFest 2023, such as food quality or venue selection
* **Product Popularity**: Analyze social media comments to gather insights on the scope of improvement of a product or check its popularity for marketing and business decisions

## Getting Started

* Clone the repository and install the required dependencies
* Run the API using `flask run`
* Send a POST request to `/analyze` with the feedback text in the request body

## API Endpoint

* `/analyze`: Analyze feedback text and return a JSON response with insights

## License

* Emosense is licensed under the MIT License
