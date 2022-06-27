import rasterio
import matplotlib.pyplot as plt
from rasterio.plot import show
from rasterio.plot import show_hist

def plot_raster(self,rast_data, title='', figsize=(10,10)):
        """
        Plots population count in log scale(+1)
        args:
            rast_data (np arrray): an array of the raster image
            title (str): the title of the image
            figsize (tuple): scale of the image to be displayed
        returns:
            pyplot image
        """
        plt.figure(figsize = figsize)
        im1 = plt.imshow(np.log1p(rast_data),) # vmin=0, vmax=2.1)

        plt.title("{}".format(title), fontdict = {'fontsize': 20})  
        plt.axis('off')
        plt.colorbar(im1, fraction=0.03)
        
        
def geo_plot(gdf:gpd.GeoDataFrame)->None:
    fig = plt.figure(figsize=(15,6))
    ax = plt.axes(projection='3d')
    ax.scatter3D(gdf.geometry.x, gdf.geometry.y, gdf.elevation, c= gdf.elevation, cmap='terrain')
    ax.set_xlabel("Longitude")
    ax.set_xlabel("Latitude")
    ax.set_zlabel("Elevation")
    plt.savefig("../files/terrain.png")
    plt.show()

def show_raster(path_to_raster):
    """
    displays a raster from a .tif raster file
    args:
        path_to_raster (str): path to the raster file
    returns:
        rasterio image
    """
    src = rasterio.open(path_to_raster)
    fig, (axrgb, axhist) = plt.subplots(1, 2, figsize=(14,7))
    show((src), cmap='Greys_r', contour=True, ax=axrgb)
    show_hist(src, bins=50, histtype='stepfilled',
            lw=0.0, stacked=False, alpha=0.3, ax=axhist)
    plt.show()