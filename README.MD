# Tab Extractor

*Extractes http/s links from .json file converted from .jsonlz4 which used by firefox to store current session including current tabs*

*Tested on windows 10 and 11*

## Usage

1. Go to [Session History Scrounger](https://www.jeffersonscher.com/ffu/scrounger.html)

2. Load your `.jsonlz4`-file. Eg. `previous.jsonlz4`

3. Extract URL by using the `Scrounge URLs`-button

4. Save file by using `Save Uncompressed JSON (sessionstore.js format)`-button

5. Save file to an approriate location

6. Run the ```exctractor.py <input> [output]```
   
   - `input` is the path to json file. Default:`./sessionstore(previous_jsonlz4).json`
   
   - `output` (optional) is path output to. Recommended .txt. Default: `./output.txt`

7. Open output file in editor

8. Highlight all (`ctrl + a`) links in the editor and drop into Firefox tab-bar. 
   
   - Done.

9. If drag and drop does not work:
   
   1. Create a bookmark folder
   2. Highlight all (`ctrl + a`) links in the editor and drop into the newly created bookmarks folder
   3. Right click bookmark folder and select "Open all Bookmarks"
   - You may recieve a confrimation that you want to open a lot of tabs, then press `Open Tabs`-button
   - Note: By loading a lot of tabs, your browser may slow down
   - Done
