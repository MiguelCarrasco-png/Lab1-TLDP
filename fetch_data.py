# # main.py
# # Import necessary libraries
# import discogs_client
# import json

# def search_discogs_and_save(query, search_type='release'):
#     """
#     query (str): The search term (e.g., an artist name, release title).
#     search_type (str): The type of search to perform (e.g., 'release', 'artist').
#     """
#     try:
#         #Initialize the Discogs API client
#         d = discogs_client.Client('ExampleApplication/0.1', user_token='nCoFlVFdXegJFzIJZsSmPWIUhSkdJQnwTRzfZbzw')

#         # Perform the search
#         # We use the client's search() method to query the Discogs database.
#         print(f"Searching for '{query}' as a '{search_type}'...")
#         results = d.search(query, type=search_type)

#         # Process and prepare the data for saving
#         # We are going to append the artist name and the title of the song of only the first page of the query.
#        if results:
#         results_data = []
#         for result in results.page(1):
#             artist_name = result.artists[0].name if result.artists else "Unknown Artist"
#             results_data.append({'title': result.title, 'artist': artist_name})
#         else:
#             print("No results found.")
#             return

#         # Print the response to the console
#         print("\n--- API Response ---")
#         print(json.dumps(results_data, indent=4))
#         print("--------------------")

#         # Save the response to a .json file
#         file_name = f"{query.replace(' ', '_').lower()}_results.json"
#         with open(file_name, 'w', encoding='utf-8') as f:
#             json.dump(results_data, f, ensure_ascii=False, indent=4)

#         print(f"\nSuccessfully saved results to '{file_name}'")

#     except discogs_client.exceptions.HTTPError as e:
#         print(f"An API error occurred: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     search_query = 'Thriller'
#     search_discogs_and_save(search_query)
import discogs_client
import json

def search_discogs_and_save(query, search_type='release'):
    """
    query (str): The search term (e.g., an artist name, release title).
    search_type (str): The type of search to perform (e.g., 'release', 'artist').
    """
    try:
        #Initialize the Discogs API client
        d = discogs_client.Client('ExampleApplication/0.1', user_token='nCoFlVFdXegJFzIJZsSmPWIUhSkdJQnwTRzfZbzw')
        
        # Perform the search
        # We use the client's search() method to query the Discogs database.
        print(f"Searching for '{query}' as a '{search_type}'...")
        results = d.search(query, type=search_type)

        # Process and prepare the data for saving
        # We are going to append the artist name and the title of the song of only the first page of the query.
        if results:
            results_data = []
            for result in results.page(1):
                artist_name = result.artists[0].name if result.artists else "Unknown Artist"
                results_data.append({'title': result.title, 'artist': artist_name})
        else:
            print("No results found.")
            return

        # Print the response to the console
        print("\n--- API Response ---")
        print(json.dumps(results_data, indent=4))
        print("--------------------")

        # Save the response to a .json file
        file_name = f"{query.replace(' ', '_').lower()}_results.json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(results_data, f, ensure_ascii=False, indent=4)

        print(f"\nSuccessfully saved results to '{file_name}'")

    except discogs_client.exceptions.HTTPError as e:
        print(f"An API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    search_query = 'Thriller'
    search_discogs_and_save(search_query)

