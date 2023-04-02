from serpapi import GoogleSearch

def search_google(query, search_type=''):
	# Set your SerpApi API key here
	GoogleSearch.SERP_API_KEY = "b32d0eb51cec3dbc12ea642eee23dbeed3245a681a3957dbef2162a15ef2bffc"
	params = {
			"engine": "google",
			"q": query,
			"filter": "0",
			"num": "10",
			"api_key": GoogleSearch.SERP_API_KEY
		}
	# Set search parameters based on search_type
	if search_type == 'videos':
		params['tbm'] = "vid"
		search_results_key = "video_results"
		result_keys = ["title", "link", "thumbnail", "snippet", "rich_snippet", "video_link"]
	
	elif search_type == 'news':
		params['tbm'] = "nws"
		search_results_key = "news_results"
		result_keys = ["title", "link", "source", "date", "snippet", "thumbnail"]

	elif search_type == 'images':
		params['tbm'] = "isch"
		params['ijn'] = "0"
		search_results_key = "images_results"
		result_keys = ["original"]
	
	else:
		search_results_key = "organic_results"
		result_keys = ["title", "link", "snippet"]

	# Create a GoogleSearch object and retrieve the search results
	search = GoogleSearch(params)
	results = search.get_dict()

	# Extract search metadata and search information
	metadata = results["search_metadata"]
	search_info = {
		"total_results": results["search_information"]["total_results"],
		"time_taken": results["search_information"]["time_taken_displayed"]
	}

	# Extract results based on search_type
	search_results = results[search_results_key]
	count = len(search_results)
	while count < 20 and "serpapi_pagination" in results:
		link_to_next_page = results['serpapi_pagination']['next_link']
		search_params = {"api_key": GoogleSearch.SERP_API_KEY}
		for key, value in params.items():
			if key != "api_key":
				search_params[key] = value
		search_params["start"] = count + 1
		search = GoogleSearch(search_params)
		results = search.get_dict()
		search_results.extend(results[search_results_key])
		count = len(search_results)

	# Extract relevant result information based on search_type
	results_list = []

	for result in search_results:
		result_info = {}
		for key in result_keys:
			if key in result:
				result_info[key] = result[key]
		results_list.append(result_info)
		print(result_info, "\n")

	return len(search_results)



print("-"*200)
print(search_google("Andrew Tate"))
print("-"*200)
print(search_google("Andrew Tate", "videos"))
print("-"*200)
print(search_google("Andrew Tate", "news"))
print("-"*200)
print(search_google("Andrew Tate", "images"))
print("-"*200)