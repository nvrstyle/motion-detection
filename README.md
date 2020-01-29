# Motion Detection
Motion detection in video stream or in video file 

Simple motion detection algorithm based on compare current and previous frame

## features
- motion detection
- selection size of moving objects for detection 

#### coming soon features
- GUI
- Change detection algorithm parameters in runtime

## Built With
* [OpenCV](https://opencv.org/) - Computer vision library
* [NumPy](https://numpy.org/) -  Scientific computing library

## Issue
*  During installation OpenCV library ` pip install opencv-python ` get error:
```sh
Could not find a version that satisfies the requirement opencv-python (from versions: )
No matching distribution found for opencv-python
```
* Answer
    * You should upgrade pip: ` pip install --upgrade pip `
      
      After upgrade pip try again install OpenCV ` pip install opencv-python `
  
* During upgrade pip it crashed and pip don't work: 
```sh
Could not install packages due to an EnvironmentError: [WinError 5]
Consider using the `--user` option or check the permissions.
```
* Answer
    * You should manually restore pip : 
    ```sh
    cd env
    curl https://bootstrap.pypa.io/get-pip.py | python `
    ```

   * After completed installation pip will work
