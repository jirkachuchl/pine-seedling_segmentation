# Pine-seedling segmentation

This project is focused on the segmentation of pine seedlings.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [License](#license)
- [Example](#example)

## Introduction

This project is focused on the segmentation of pine seedlings. We have many photos of planters with pine seedlings from three populations of Scots pine (Pinus sylvestris). The main goal is to standardize images to make them comparable, segment seedlings, and determine their average color.

As first input into this process the it is optimal to use some of the formats with lossless compression. Ideally, it could be obtained from a raw file (e.g., DNG, RAW...) applying only minimal necessary processing (demosaicing, color space conversion, and linearization). Avoid applying tone curves, sharpening, or other artistic adjustments during this step to preserve data integrity. Based on your format, it is necessary to edit the extension in the code to the one you are using.

## Features

List key features of your project.

- [Standardization of images using white reference](./1_standardization)
- [Image transformation](./2_transformation)
- [Image splitting](./3_splitting)
- [Image segmentation using YOLOv7](./4_segmentation)
- [Backround removal](./5_backround_removal)
- [Image composing](./6_composing)
- [Overlay of individual outputs](./7_overlaying)
- [Identification of individual seedlings and acquisition of RGB values](./8_RGB_acquisition)

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Example
<div align="center">
    <a href="/output/1_output.png">
        <img src="/output/1_output.png" width="79%"/>
    </a>
</div>
