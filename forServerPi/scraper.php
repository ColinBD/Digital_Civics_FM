<?php
#Include the script 'emoji' which parses a string to remove emoji codes
include('emoji/emoji.php');

#Returns a JSON from a non-private IG account page
function scrape_insta($username) {
	$insta_source = file_get_contents('http://instagram.com/'.$username);
	$shards = explode('window._sharedData = ', $insta_source);
	$insta_json = explode(';</script>', $shards[1]); 
	$insta_array = json_decode($insta_json[0], TRUE);
	return $insta_array;
}

#Array of accounts to scrape
$accounts_for_scraping = array('newcastleuni','nclalumni','newcastleuniapl','newcastleunildn','musicncl');

foreach($accounts_for_scraping as $account)
{	
	#Make directory for each account
	mkdir('/home/pi/sync/pictures/' . $account);
	
	#Scrape the accounts
	$results_array = scrape_insta($account);
	
	#Create array to hold picture information
	$info = array();
	
	#Picture Number varible set to 0
	$no = 0;

	#for each element of the array returned (12 elements per account)
	 for($cnt=0; $cnt < 12; $cnt++)
		{
			#Reset picture number so that it starts at 1 and not 0 (for renaming purposes)
			$no = $no + 1;
			
			#Create an array to store scraped results
			$latest_array = $results_array['entry_data']['ProfilePage'][0]['user']['media']['nodes'][$cnt];
			
			#Set the directory and name of each image to be scraped
			$directory = '/var/www/html/pictures/' . $account . '/' . $account . '_' . $no . '.jpeg';

			#Save each picture from URL to directory
			file_put_contents($directory, file_get_contents($latest_array['display_src']));
			
			#Check to see whether the picture has a caption or not
			if(isset($latest_array['caption'])) #If the picture has a caption
			{
				#Save caption to string variable
				$caption = $latest_array['caption'];
				#Run caption through emoji parser
				$caption = emoji_unified_to_html($caption);	
				#Strip tags from caption 
				$caption = strip_tags($caption);
			}
			else
			{
				#Else the file has no caption, so set caption to say 'No caption'
				$caption = "This image has no caption";
			}	
			
			#Set picture information to variables
			$name = $account . '_' . $no;
			$date_posted = $latest_array['date'];
			$likes_no = $latest_array['likes']['count'];
			$comment_no = $latest_array['comments']['count'];
			
			#Put all the picture information for a single image in one temporary array
			$temp = array($name,$date_posted,$comment_no,$likes_no,$caption);
			
			#Refer to each item in the array as a list so it can be accessed later using something like $array[0][1]
			list($a[0], $a[1], $a[2], $a[3], $a[4]) = $temp;
			
			#Push temporary array to info array
			array_push($info,$temp);

	}
	
	#directory for saving picture information
	$dir = '/var/www/html/pictures/' . $account . '/' . $account . '.json';
	
	//var_dump($info[4][4]);
	
	#Encode the info array of picture information to type JSON and save to the directory above. 
	file_put_contents($dir, json_encode($info));
}
?>
