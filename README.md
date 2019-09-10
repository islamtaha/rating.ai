# rating.ai

rating.ai is project Sentiment analysis and ratings for a product from facebook group posts and twitter tweets to gain Intuition what the users feedback on the product based on facebook group posts and help to know more about negative feedback.


# Usage

1. go to https://islamtaha.github.io/rating.ai/
2. enter the search keyword and count(the number of tweets returned)
3. click search

**Deployment**
----
* **Backend**
	
	backend is deployed on heroku 

	link to application: https://rating-api.herokuapp.com/

* **Frontend**
	
	frontend is deployed on github 

	link to application: https://islamtaha.github.io/rating.ai/


**Rest Api Endpoints**
----	
* **Twitter Search and Prediction Api**
	----
  	Returns an array of json data about tweets that has the search keyword in it combined with the rating prediction.

	* **URL**

  		twitter/:search_keyword/:count

	* **Method:**

  		`GET`
  
	*  **URL Params**

   		**Required:**
 
   		`search_keyword=[string]`
   		`count=[integer]`

	* **Data Params**

  		None

	* **Success Response:**

  		* **Code:** 200 <br />
    	**Content:** `[{tweet json returned from twitter search}, prediction]`
 
	* **Sample Call:**

  	```javascript
    	$.ajax({
      	url: "https://rating-api.herokuapp.com/twitter/trump/1",
      	dataType: "json",
      	type : "GET",
      	success : function(r) {
        	console.log(r);
      	}
    	});
  	```

# To-do List

- [ ] increase twitter model accuracy and make the result based on the search keyword context
- [ ] implement facebook Api and model
