# artworks-recognition
Pattern recognition system of artworks using Python and OpenCV

The aim of the proposed system is to analyze the query image and look for possible matches, and then similarity, with artworks in the database in order to identify false copyright and prevent intellectual property theft. This system was developed for my Bachelor Thesis (read more [here](https://drive.google.com/file/d/0B1qdoPYeXd80cnplMzNIQjZSSk0/view)) and was integrated in Art Everywhere, an Android application where young artists can share and promote their artworks. 

Usage
==============
<i>python search.py --db artworks.csv --artworks artworks --query queries/query01.png</i>

Some results
==============
- Image1

![Image1](https://github.com/kuka93/artworks-recognition/blob/master/query07.png)

It was detected similarities with the Mona Lisa by Leonardo Da Vinci and the percentage of detected similarity is 82.98%.
![Res1](https://github.com/kuka93/artworks-recognition/blob/master/res1.jpg)

- Image2

![Image2](https://github.com/kuka93/artworks-recognition/blob/master/query08.png)

It was detected similarities with the Mona Lisa by Leonardo Da Vinci and the percentage of detected similarity is 86.87%.
![Res2](https://github.com/kuka93/artworks-recognition/blob/master/res2.jpg)
