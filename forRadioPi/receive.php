<?php
	#Set variable count to 0
	$count = 0;
		
	#location of r-synced images 
	$folders = scandir('/var/www/html/pictures/');
	#For each folder wihtin the above directory 
	foreach($folders as $folder) 
	{	
		 #Increment count by one
		 $count = $count + 1;
		 
		 #If count is more than 2 (skips over the . & .. you get when returning files in a directory)
		 if($count > 2)
			 
		 {
			#Set the directory locations 
			$datadir =  '/var/www/html/pictures/' . $folder . '/' . $folder . '.json';
			
			#Get the contents of the directory and save to variable $json
			$json = file_get_contents($datadir);
			
			#Decode the $json variable 
			$data = json_decode($json);
			
			#Put the contents of the $json variable into another folder called save (every json file to go into the same folder)
			file_put_contents('/var/www/html/saved/' . $folder . '.json',$json);		
			
			#For each picture within the folder...(of which there are 12)
			for($cnt=1; $cnt < 13; $cnt++)
			{
				#Define the directory (notice .jpeg instead of .json at the end)
				$source = '/var/www/html/pictures/' . $folder . '/' . $folder . '_' . $cnt .'.jpeg';
				
				#Define the save location(all .jpeg's saved to one folder)
				$destination = '/var/www/html/saved/' . $folder . '_' . $cnt .'.jpeg';
				
				#If the image already exists in saved... (this should never happen!)
				if (!copy($source, $destination)) 
				{
					#Echo this error
					echo "failed to copy $source...\n";
				}
				
			}

		}
	}
?> 
