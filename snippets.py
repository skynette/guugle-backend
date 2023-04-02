from serpapi import GoogleSearch

def search_google(query):
	GoogleSearch.SERP_API_KEY = "b32d0eb51cec3dbc12ea642eee23dbeed3245a681a3957dbef2162a15ef2bffc"

	params = {
		"engine": "google",
		"q": query,
		"filter": "0",
		"num": "10"
	}

	search = GoogleSearch(params)
	results = search.get_dict()
	metadata = results["search_metadata"]
	search_info = {}
	search_info["total_results"] = results["search_information"]["total_results"]
	search_info["time_taken"] = results["search_information"]["time_taken_displayed"]
	organic_results = results["organic_results"]
	count = len(organic_results)

	while count < 20:
		link_to_next_page = results['serpapi_pagination']['next_link']
		search = GoogleSearch({"engine": "google", "q": query, "filter": "0", "start": count+1, "num": "10"})
		results = search.get_dict()
		organic_results.extend(results['organic_results'])
		count = len(organic_results)

	for i in organic_results:
		title = i["title"]
		link = i["link"]
		snippet = i["snippet"]

	return len(organic_results)



def search_google_images(query):
	# Set your SerpApi API key here
	GoogleSearch.SERP_API_KEY = "b32d0eb51cec3dbc12ea642eee23dbeed3245a681a3957dbef2162a15ef2bffc"

	# Set search parameters
	params = {
		"engine": "google",
		"q": query,
		"tbm": "isch",  # Set the search type to image search
		"ijn": "0",     # Set the initial page number to 0
		"api_key": GoogleSearch.SERP_API_KEY
	}

	# Create a GoogleSearch object and retrieve the search results
	search = GoogleSearch(params)
	results = search.get_dict()

	# Extract image URLs from the search results
	image_urls = []
	for image_result in results["images_results"]:
		if "original" in image_result:
			image_urls.append(image_result["original"])
	print(image_urls)
	return len(image_urls)



def search_video(query):
	GoogleSearch.SERP_API_KEY = "b32d0eb51cec3dbc12ea642eee23dbeed3245a681a3957dbef2162a15ef2bffc"

	params = {
		"engine": "google",
		"q": query,
		"tbm": "vid",
		"filter": "0",
		"num": "10"
	}

	search = GoogleSearch(params)
	results = search.get_dict()
	metadata = results["search_metadata"]
	search_info = {}
	search_info["total_results"] = results["search_information"]["total_results"]
	search_info["time_taken"] = results["search_information"]["time_taken_displayed"]
	video_results = results["video_results"]
	count = len(video_results)

	while count < 20:
		link_to_next_page = results['serpapi_pagination']['next_link']
		search = GoogleSearch({"engine": "google", "q": query, "tbm": "vid", "filter": "0", "start": count+1, "num": "10"})
		results = search.get_dict()
		video_results.extend(results['video_results'])
		count = len(video_results)

	for i in video_results:
		title = i["title"]
		link = i["link"]
		thumbnail = i["thumbnail"]
		snippet = i["snippet"]
		rich_snippet = i.get("rich_snippet", None)
		video_link = i.get("video_link", None)

		res = {
			"title": title,
			"link": link,
			"thumbnail": thumbnail,
			"snippet": snippet,
			"rich_snippet": rich_snippet,
			"video_link": video_link,
		}
		print(res, "\n")
		
	return len(video_results)


def search_news(query):
	GoogleSearch.SERP_API_KEY = "b32d0eb51cec3dbc12ea642eee23dbeed3245a681a3957dbef2162a15ef2bffc"

	params = {
		"engine": "google",
		"q": query,
		"tbm": "nws",
		"num": "10"
	}

	search = GoogleSearch(params)
	results = search.get_dict()
	metadata = results["search_metadata"]
	search_info = {}
	search_info["total_results"] = results["search_information"]["total_results"]
	search_info["time_taken"] = results["search_information"]["time_taken_displayed"]
	news_results = results["news_results"]
	count = len(news_results)

	while count < 20:
		link_to_next_page = results['serpapi_pagination']['next_link']
		search = GoogleSearch({"engine": "google", "q": query, "tbm": "nws", "start": count+1, "num": "10"})
		results = search.get_dict()
		news_results.extend(results['news_results'])
		count = len(news_results)

	for i in news_results:
		title = i["title"]
		link = i["link"]
		source = i["source"]
		date = i["date"]
		snippet = i["snippet"]
		thumbnail =i['thumbnail']
		res = {
			"title": title,
			"link": link,
			"source": source,
			"date": date,
			"snippet": snippet,
			"thumbnail": thumbnail
		}
		print(res, "\n")
		
	return len(news_results)
