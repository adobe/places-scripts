Places Import script
=================
A Python script is used to simplify the batch import of points of interest (POIs) from a .csv file into a Places database by using the Places REST APIs.

## CSV file

A sample .csv file, `places_sample.csv`, is part of this package and includes the required headers and a row of sample data. These headers are all lower case and correspond to the reserved metatdata keys that are used in the Places database. When you add headers, the additional columns are added to the Places database in a separate metadata section for each POI as key/value pairs.

Here is a list of the columns and the values that you need to use:

* lib_id

  A valid library ID that is obtained from Places database.

* type

  Point is currently the only valid value.

* longitude

  A value between -180 and 180.

* latitude

  A value between -85 and 85.

* radius

  A value between 10 and 2000.

**Column values**

The values of the following columns are used in the Places UI:
  
* color, which is used as the color of the pin that represents the location of the POI in the Places UI map.
  - The valid values are "", #3E76D0, #AA99E8, #DC2ABA, #FC685B, #FC962E, #F6C436, #BECE5D, #61B56B, and #3DC8DE.
  - If the value is left blank, the UI uses blue as the default color.
    
    The values correspond to blue, purple, fuschia, orange, light orange, yellow, light green, green, and light blue, respectively.
  
* icon, which is used as the icon on the pin that represents the location of the POI on the Places UI map
  - The valid values are "", anchor, beaker, bell, browse, book, brush, building, calculator, camera, shoppingCart, clock, box, flashlight, follow, bid, ribbon, education, hammer, heart, home, key, mailbox, male, promote, money, trap, game, gift, launch, star, lightbulb, pin, target, teapot, thumbDown, thumbUp, briefcase, trophy, female, and wrench.
  - If the value is left blank, the UI uses star as the default icon.

* Columns that are not mentioned can be left blank.


Running the Script
-------------
1. Download files to the appropriate directory.
1. In a text editor, open the `config.py` file and complete the following tasks:
   1. Edit the following variable values as strings:

      * `csv_file_path`

        The path to your csv file.

      * `access_code`
      
        This is your access code obtained from the call to Adobe IMS.
      
      * `org_id`
      
        The Experience Cloud orgID into which the POIs are to be imported.
      
      * `api_key`
      
        This is your Places REST API key obtained from your AdobeIO Places Integration.

    1. Save your changes.
1. In a terminal window, navigate to the `…/places-scripts/import/` directory.
1. Enter `python ./places_import.py` and press the **enter** (**return**) key.


Pre-import CSV checks
------------
The script initially completes the following checks on the .csv file:

- Whether a `.csv` file was specified.
- Whether the file path is valid.
- Whether the reserved metatdata headers are included.

  The reserved metadata headers are lib_id, name, description, type, longitude, latitude, radius, country, state, city, street, category, icon, and color.

  **Tip**: The headers are all lower case and can be listed in any order.

- Verifies the values of the columns specified in the CSV file section.

If errors are found, the script prints out the errors and is aborted. If no errors are found, the script attempts to import the POIs in batches of 1000. If the batch is successfully imported, the script reports a status code of 200. If the batch is not successfully imported, errors are reported.

## Unit Tests

Unit tests are in the `tests.py` file, should be run before each pull request, and should all pass. Additional tests should be added with new code. To run the tests, navigate to the `…/places-scripts/import/` directory, and enter `python ./places_import.py` in terminal.


License
-------
This project is licensed under the Apache V2 License. For more information, see [LICENSE](../LICENSE.md).

