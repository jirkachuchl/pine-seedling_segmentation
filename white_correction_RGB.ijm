vystup = getInfo("image.filename");
vystup = substring(vystup, 9, indexOf(vystup, "."));
outputFilePath = "D:/jirka/Documents/skola/Ing/DP/srpen_sadbovace/corrected_srpen/"+vystup+"_corrected.png"

run("Duplicate...", "title =1");
name=getTitle();
selectImage(name);
name="1"
rename(name);
run("Split Channels");

// Get the current slice (channel) and perform white correction
selectImage("1 (red)");
name = "Red"
rename(name);"
run("Clear Results");
roiManager("Select", 0);
roiManager("Measure");
meanR = getResult("Mean", 0);
val = 255/meanR
run("Select None");
selectImage("Red");
run("Multiply...", "value="+val);

selectImage("1 (green)");
name = "Green"
rename(name);"
run("Clear Results");
roiManager("Select", 0);
roiManager("Measure");
meanG = getResult("Mean", 0);
val = 255/meanG
run("Select None");
selectImage("Green");
run("Multiply...", "value="+val);

selectImage("1 (blue)");
name = "Blue"
rename(name);"
run("Clear Results");
roiManager("Select", 0);
roiManager("Measure");
meanB = getResult("Mean", 0);
val = 255/meanB
run("Select None");
selectImage("Blue");
run("Multiply...", "value="+val);

run("Merge Channels...", "red=Red green=Green blue=Blue create");
run("Stack to RGB");

saveAs("Png", outputFilePath);
close("*");
roiManager("delete");
run("Clear Results");

