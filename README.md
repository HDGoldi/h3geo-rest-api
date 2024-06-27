# h3geo-rest-api
Rest API for LatLng to H3 Index Cell. Build to be a simple lookup API. 


Feature to build next: GeoIndex API Endpoint

**Description:**
Develop a simple API endpoint using Flask or FastAPI (Python frameworks) that receives three parameters via a GET request: longitude, latitude, and resolution (an integer representing the resolution size). Utilizing the Uber H3 Geo library, this endpoint will calculate the corresponding H3 cell index based on the provided longitude and latitude at the specified resolution. It should return this H3 cell index in a JSON format.

**Acceptance Criteria:**
- The API must correctly accept longitude, latitude, and resolution as query parameters.
- Utilize the Uber H3 library to calculate the correct cell index based on the input parameters.
- updated the `/geoindex` endpoint to accept `longitude`, `latitude`, and `resolution` as a JSON body in a POST request instead of query parameters in a GET request
- Return the H3 cell index in a JSON response in the format: { "h3Index": "<calculated_cell_index>" }.
- Ensure input validation for the query parameters: longitude and latitude should be valid geographical coordinates, and resolution should be an integer within the H3 library's allowed resolution range.
- Construct the API in a way that it can easily be expanded with more functionality.
- updated the `/geoindex` endpoint to include API key authorization. The endpoint now requires an API key to be passed in the header as `X-API-Key`. Please provide the API key in the `Env Secrets` tab with the key name `API_KEY`. Test the app and let me know if you need any further adjustments.

**Notes:**
- This feature serves as a fundamental building block for larger, more complex features that involve geospatial data processing.
- Ensure the code is well-documented, making it easier for future developers to understand and build upon.
- This implementation should consider any potential error handling, such as invalid input values or server errors, returning user-friendly error messages when necessary.
