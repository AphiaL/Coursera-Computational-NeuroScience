## Simple Models
### Basic coding models: 
```
1. linear response
The response of the time is highly dependent upon the stimulus of the time.
s(t) -> r(t)
```
### 2. Temporal filtering
> An intuitive way to think of temporal filtering is to imagine that 
the system is scanning the stimulus wave-form by sliding a 
window of a certain width/duration along it. The more the 
stimulus in the window resembles the filter, the more strongly the 
system will respond. Thus, the system is “looking for” pieces of the 
stimulus that resemble the filter.
![](http://geekresearchlab.net/coursera/neuro/simple-models-1.jpg)<br>
#### Question:
Since this is a linear system, 
which of the following will always be true?
#### Answers:
(i) If you scale the input by a constant, the output will be scaled by the same constant. 
(ii) The output of a sum of different inputs is equal to the sum of the outputs of each of the individual inputs.

```
Examples of temporal filtering:
1. Calculating average
2. Calculating leaky average
```
### 3. Spatial filtering
Hint: Apply temporal filtering to the time
> Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object, for example, filtering video data received from satellite and space probes, or removal of raster from a television picture or scanned image. In digital image processing, the term image refers to a two-dimensional light-intensity function, where amplitude at spatial coordinates (x,y) gives the intensity (brightness) of the image at that point.
![](http://geekresearchlab.net/coursera/neuro/simple-models-2.jpg)<br>
Spatial filtering and retinal receptive fields:
[1] <a href="http://en.wikibooks.org/wiki/Sensory_Systems/Visual_System#Signal_Processing">WikiBooks</a><br>
[2] <a href="http://docs.gimp.org/2.6/en/plug-in-dog.html">Spatial Filtering</a><br>
<br>
![](http://geekresearchlab.net/coursera/neuro/simple-models-3.jpg)<br>

### 4. Spatiotemporal filtering

<br>![](http://geekresearchlab.net/coursera/neuro/simple-models-4.jpg)<br>

#### Question:
Which of the following inputs might cause a linear system with a positive filter to predict a negative firing rate?

#### Answer:
An input that slowly varies between a large positive value and a large negative value.

### Nonlinearity function
![](http://geekresearchlab.net/coursera/neuro/simple-models-5.jpg)

```
How to find the components of this model?
This will be continued in the next chapter...
```
