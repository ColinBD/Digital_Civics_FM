<?php
	#Set variable count to 0
	$count = 0;
	#New array called accounts
	$accounts = array();
	
	#Set directory for folders 
	$folders = scandir('/var/www/html/pictures/');
	
	#New array called account_info
	$account_info = array();
	
	#Fror each folder found within pictures...
	foreach($folders as $folder) 
	{
		#Increment count by one each time 
		 $count = $count + 1;
		  #Return everything after the . & .. returned by scanning a a directory
		 if($count > 2)
		 
		 {
			 #Define directory for pictures 
			$datadir =  '/var/www/html/pictures/' . $folder . '/' . $folder . '.json';
			
			#Combine all JSON files into one big JSON 
			# K=>folder name, value => json$$
			array_push($account_info, array('name' => $folder,
			                                'data' => json_decode(file_get_contents($datadir), true)));
				
			#Push folder name to accounts array
			array_push($accounts, $folder);
			
			#For each picture within the folder...
			for($cnt=1; $cnt < 13; $cnt++)
			{
				#Define source of picture
				$source = '/var/www/html/pictures/' . $folder . '/' . $folder . '_' . $cnt .'.jpeg';
				
				#Define destination of pictures 
				$destination = '/var/www/html/saved/' . $folder . '_' . $cnt .'.jpeg';
				
				#If image already exists (should never happen!)
				if (!copy($source, $destination)) 
				{
					#Echo error message
					echo "failed to copy $source...\n";
				}
				
			}

		}
	}
	
	#Put the contents of account info into a single file named accounts.json
	file_put_contents('/var/www/html/saved/accounts.json',json_encode($account_info));

	#Directory to look in
	$directory = '/var/www/html/saved/';
	
	#Search for files ending in .jpeg
	$files = glob($directory . '*.jpeg');

	if ( $files !== false )
	{
		#Count number of files in that directory
		$filecount = count( $files );
		//echo $filecount;
	}
	
	#new array to hold each image's directory 
	$images = array();
	
	#For every picture found when counting
	for($cnt=0; $cnt < $filecount; $cnt++)
	{
		#Define new directory 
		$imagesDir = 'saved/';

		#find all .jpeg images
		$images = glob($imagesDir . '*.{jpeg}', GLOB_BRACE);

		#Set randomImage to $images 
		$randomImage = $images[array_rand($images)];
		
		#If the picture is not already in the array of random images
		if (!in_array($randomImage, $images)) 
		{
			#Add the image to the array
			array_push($images, $randomImage);
		}
	}
	
	#We now have an array of all images held in array $images
	
	shuffle($images); #Shuffle Images randomly	in array
	
	#Prepare for writing a HTML file - open index.html
	$myfile = fopen("/var/www/html/index.html", "w") or die("Unable to open file!");
	
	#CSS & html headers etc...
	$txt = 
	"<html>
	<head>
	<style>
	html, body, #wrapper {
	height:100%;
	width: 100%;
	margin: 0;
	padding: 0;
	border: 0;
	background-color: #331200;
	 overflow-y:hidden;
	 cursor: none;
	}
	
	#wrapper td {
	background-color: #331200;
	vertical-align: middle;
	text-align: center;
	cursor: none;
	}

	#wrapper img {
	max-height: 600px;
	max-width: 70%;
	cursor: none;
	}
	
	.mySlides {display:none;}
	</style>
	</head>
	<body>
	<table id='wrapper'>
	<tr>
	<div class='w3-content w3-section' style='max-width:500px; max-height:600px'> \n<td>";
	
	#Write to file
	fwrite($myfile, $txt);
	
	#For each image in the image array (randomised list of images...)
	foreach ($images as $image) 
	{
		#Add ' to image name for putting into image tag in html
		$image = "'" . $image . "'";
		
		#put in variable
		$write1 = "        <img class='mySlides' src=" . $image . " style='width:100%; border-radius:10px;'> \n";
		
		#data['ncl']['data']['ncl_5']['capation']
		
		#Strip ' from image name
		$image = str_replace("'", '', $image);
		
		#Strip saved/ from image name
		$image = str_replace('saved/', '', $image);
		
		#strip .jpeg from image name
		$account = str_replace('.jpeg','',$image); #newcastleuni_5
		
		#Strip image number from image name 
		$stripped = preg_replace('/[0-9]+/', '', $account);
		
		#Strip underscrore from image name
		$stripped = str_replace('_','',$stripped);	#newcastleuni
		
		#For each record in account_info...
		foreach ($account_info as $record) 
		{
			#If the stripped variable equals the account name e.g. newcastleuni
			if($record['name'] == $stripped)
			{
				# datum is an array containing meta-data for an account
				foreach($record['data'] as $datum)
				{
					if ($datum[0] == $account)
					{
						$caption =  $datum[4] . "\n\n";
						#Caption for each image if needed
					}	
				}
			}
		}
		
		#Write html image src to index.html
		fwrite($myfile, $write1);
			
	}
	
	#end div
	$div = "		</td></div>
	      </tr>
   </table></div>\n";
   
   #write div to file
	fwrite($myfile, $div);
	
	#write <script> tag
	$end = "
	<script>
		var myIndex = 0;
		carousel();

		function carousel() {
		var i;
		var x = document.getElementsByClassName('mySlides');
		for (i = 0; i < x.length; i++) {
		   x[i].style.display = 'none';  
		}
		myIndex++;
		if (myIndex > x.length) {myIndex = 1}    
		x[myIndex-1].style.display = 'block';  
		setTimeout(carousel, 30000); // 30 seconds per image
		}
	</script>\n";
	
	#Save to index.html
	fwrite($myfile, $end);
	
	#End html file
	$divend = "	</body>\n</html>";
	
	#write to file
	fwrite($myfile, $divend);
	
	#Close the file - done with it. 
	fclose($myfile);
	
?>
