class CameoDepth(Cameo):    
	def __init__(self):        
		self._windowManager = WindowManager('Cameo',                                           self.onKeypress)        
		device = depth.CV_CAP_OPENNI # uncomment for Microsoft Kinect        
		#device = depth.CV_CAP_OPENNI_ASUS # uncomment for Asus Xtion        
		self._captureManager = CaptureManager(cv2.VideoCapture(device), self._windowManager, True)        		self._faceTracker = FaceTracker()        
		self._shouldDrawDebugRects = False        
		self._curveFilter = filters.BGRPortraCurveFilter()    
	def run(self):        
		"""Run the main loop."""        
		self._windowManager.createWindow()        
		while self._windowManager.isWindowCreated:            
			self._captureManager.enterFrame()            
			self._captureManager.channel = \                
				depth.CV_CAP_OPENNI_DISPARITY_MAP            
			disparityMap = self._captureManager.frame            
			self._captureManager.channel = \                
				depth.CV_CAP_OPENNI_VALID_DEPTH_MASK            
			validDepthMask = self._captureManager.frame            
			self._captureManager.channel = \                
				depth.CV_CAP_OPENNI_BGR_IMAGE            
			frame = self._captureManager.frame
		 self._faceTracker.update(frame)            
		 faces = self._faceTracker.faces            
		 masks = [                
				depth.createMedianMask(disparityMap, validDepthMask, face.faceRect) \                				for face in faces            
			 ]            
			rects.swapRects(frame, frame,[face.faceRect for face in faces], masks)            			filters.strokeEdges(frame, frame)            
			self._curveFilter.apply(frame, frame)            
			if self._shouldDrawDebugRects:                
				self._faceTracker.drawDebugRects(frame)            			self._captureManager.exitFrame()            
			self._windowManager.processEvents() 
if __name__=="__main__":     
	CameoDepth().run() # uncomment for depth camera 