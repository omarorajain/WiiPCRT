## The tool to generate a master key to unlock your parental controls on your Wii!

##### (...Inspired by a Wii I bought second-hand which had a parental-control pin set...)

# How it works:
1. Navigate to the Wii Menu by pressing the HOME button on a Wii Remote and selecting "Wii Menu."
2. Look at the date and time displayed on the Wii Menu and ensure they are correct. If incorrect, they will need to be changed in order for you to complete the PIN reset process. You will not be able to reset the PIN until the date is correct. [[HOW TO]](http://en-americas-support.nintendo.com/app/answers/detail/a_id/1776)
3. Select the Wii Options icon in the lower-left corner of the Wii Channel Menu.
4. Select "Wii Settings."
5. Click on the blue arrow to reach the Wii System Settings 2 menu options.
6. Select "Parental Controls," then "Yes."
7. Select "I forgot."
8. Select "I forgot." again.
9. A screen (as pictured below) with an 8 digit request code will appear, write it down!
10. Download the latest release of WiiPCRT [HERE](https://github.com/sindastra/WiiPCRT/releases).
11. Open a CMD (Command Prompt) and navigate to the folder where you downloaded the reset_tool to.
12. Run the reset_tool and pass the request code you wrote down as argument.

### Example (in CMD):
```
> reset_tool.exe 12345678
```

13. Choose the master key based on your time zone (date) from the output.
14. Enter the master key into your Wii.

### Enjoy your unlocked Wii!

# Additional notes:

* If you get any errors about missing DLLs, try installing the vcredist files (all of them) from [HERE](https://github.com/sindastra/WiiPCRT/releases).
* Yes, this runs under wine, if you must..
* The button at the top leads to the GitHub page... You can report bugs/issues there!
* This is what a request code screen looks like on your Wii:

![sample-screen](request_sample.png "Screen on your Wii")

###### Copyright (C) 2018 Sindastra. All rights reserved. This site is not affiliated with Nintendo.
