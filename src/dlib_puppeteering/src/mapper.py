#!/usr/bin/env python3
import sys
import rospy

import roslib
#import cv2

from pau2motors.msg import pau
from dlib_puppeteering.msg import lm_points
roslib.load_manifest('dlib_puppeteering')

import random
import numpy
import numpy as np
from sklearn.linear_model import Ridge

class dlib_puppeteering:
  
  # declare publishers, subscribers, and other important static variables
  def __init__(self):
  
    self.once = 0
    self.dlibX = []
    self.dlibY = []

    self.dlibFaceIndex = []
    self.indexes_brow = [0, 1]  # shapekey indexes to be mapped
    self.indexes_mouth = [30]
    self.indexes_lipupperleft= [24, 26, 28] #[30, 32]
    self.indexes_smileleft= [30]#[24, 25, 30, 31]
    self.indexes_smileright= [31]#[24, 25, 30, 31]
    self.indexes_lowerlipdown = [36, 38, 40]

    self.pub_pau = rospy.Publisher('/blender_api/set_pau', pau, queue_size=10)
    self.image_sub = rospy.Subscriber("/dlib_values", lm_points, self.dlib_callback)

    self.blendshape_names = ['brow_center_UP', 'brow_center_DN', 'brow_inner_UP.L', 'brow_inner_DN.L', 'brow_inner_UP.R',
                          'brow_inner_DN.R', 'brow_outer_UP.L', 'brow_outer_DN.L', 'brow_outer_up.R', 'brow_outer_DN.R',
                          'eye-flare.UP.L', 'eye-blink.UP.L', 'eye-flare.UP.R', 'eye-blink.UP.R', 'eye-blink.LO.L',
                          'eye-flare.LO.L', 'eye-blink.LO.R', 'eye-flare.LO.R', 'wince.L', 'wince.R', 'sneer.L',
                          'sneer.R', 'eyes-look.dn', 'eyes-look.up', 'lip-UP.C.UP', 'lip-UP.C.DN', 'lip-UP.L.UP',
                          'lip-UP.L.DN', 'lip-UP.R.UP', 'lip-UP.R.DN', 'lips-smile.L', 'lips-smile.R', 'lips-wide.L',
                          'lips-narrow.L', 'lips-wide.R', 'lips-narrow.R', 'lip-DN.C.DN', 'lip-DN.C.UP', 'lip-DN.L.DN',
                          'lip-DN.L.UP', 'lip-DN.R.DN', 'lip-DN.R.UP', 'lips-frown.L', 'lips-frown.R','lip-JAW.DN']
    
    #x_normalized = 'hello'
    '''y_normalized = normalize(self.dlibY)
    xy = x_normalized + y_normalized
    xy = np.array(xy)
    browsup_model = Ridge(alpha = alpha)
    browsup_model.coeff_ = coeff_brows_up
    browsup_model.intercept_ = intercept_brows_up
    alpha = 0.1
    ridge = Ridge(alpha = alpha)''' 
  
  # callback: gets relative distance of DLIB's land marks per their corresponding shapekey
  def dlib_callback(self, data):
      '''print('hello_callback')

      coeff_brows_up = ([-0.03994529,  0.05965983,  0.26604942, -0.10001976,  0.02571235,
       -0.15743366, -0.15107966,  0.05932797, -0.04445027, -0.00051184,
       -0.01794235,  0.08205211, -0.02737744, -0.04503058,  0.00097107,
        0.03430173,  0.00135388,  0.12086409,  0.24367876,  0.12423624,
        0.12427326, -0.12390761,  0.16738411, -0.03294159, -0.02225945,
       -0.09150146, -0.05671128,  0.00994966, -0.0041362 ,  0.11825082,
       -0.07925411, -0.08126947, -0.05907555, -0.09782393,  0.04432068,
       -0.0397211 , -0.09751762, -0.17953067,  0.06043592,  0.10127657,
        0.02658325, -0.07335536, -0.21000558,  0.04144996, -0.01290343,
        0.06514291,  0.00780998,  0.01651065,  0.19827989, -0.00394886,
        0.00552164, -0.20197584,  0.02243605, -0.0724711 , -0.15828425,
        0.00535809,  0.10761565, -0.02992744,  0.07518744,  0.13417684,
        0.00995507,  0.08043928,  0.14559729, -0.07282683, -0.01328051,
        0.0701037 ,  0.01477559,  0.0152705 , -0.14343098,  0.15201524,
       -0.14463469,  0.02412382,  0.0697816 ,  0.00741937,  0.00819093,
       -0.03161338, -0.11183878, -0.00521626, -0.0349472 ,  0.08937093,
        0.02370157,  0.05277089, -0.0681871 ,  0.02369042, -0.05190085,
        0.05925793,  0.1404831 ,  0.05088367, -0.29246621, -0.09831926,
       -0.10359141, -0.04927141, -0.04304857,  0.18312706,  0.13543494,
       -0.18588968, -0.02794997, -0.13353171, -0.00807263, -0.1083353 ,
        0.12407571,  0.02983456,  0.16133227, -0.15397156, -0.12894383,
       -0.08374003, -0.03608447, -0.03653539, -0.08866398, -0.05310818,
       -0.08937821,  0.03761951,  0.13386111, -0.11045425,  0.03025596,
        0.047111  ,  0.060447  , -0.01068462,  0.0219471 , -0.01606329,
        0.14224367,  0.16036216, -0.03929058,  0.06096333, -0.06239731,
        0.07814062,  0.07903677,  0.10244747,  0.04471812, -0.04535393,
        0.01450537,  0.01261773,  0.0079287 , -0.09126498,  0.00105649,
       -0.10070298])
      coeff_brows_up = numpy.array(coeff_brows_up)

      intercept_brows_up = 0.24949174560098603'''

      self.dlibX = data.dlib_X
      self.dlibY = data.dlib_Y
      self.dlibFaceIndex = data.dlib_face_index

      head_pau = pau()

      head_pau.m_headRotation.x = 0.9
      head_pau.m_headRotation.y = 0.5
      head_pau.m_headRotation.z = 0.7
      head_pau.m_headRotation.w = 0.9

      head_pau.m_headTranslation.x =0.9
      head_pau.m_headTranslation.y =0.7
      head_pau.m_headTranslation.z =0.8

      head_pau.m_neckRotation.x= -0.9
      head_pau.m_neckRotation.y= -0.5
      head_pau.m_neckRotation.z= 0.5
      head_pau.m_neckRotation.w= 0.9

      head_pau.m_eyeGazeLeftPitch = 0.01
      head_pau.m_eyeGazeLeftYaw = 0.1
      head_pau.m_eyeGazeRightPitch = 0.01
      head_pau.m_eyeGazeRightYaw = 0.1

      head_pau.m_shapekeys = self.blendshape_names
      head_pau.m_coeffs = self.doMapping()

      self.pub_pau.publish(head_pau) # publish to "/blender_api/set_pau"

     


  def ridge_lipupperleft(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/lipupperleft_m_dlib.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/lipupperleft_m_fs.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:200], fs_array[0:200])
      return ridge


  '''def ridge_leftsmile(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_dlib_xy.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_left.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:300], fs_array[0:300])
      return ridge'''

  def ridge_leftsmile(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_newL.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_left.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:300], fs_array[0:300])
      return ridge


  def ridge_rightsmile(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_new1.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_new/smile_newR_fs.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:300], fs_array[0:300])
      return ridge


  def ridge_openlowerlip(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/open_dlib.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/lipslowerdown_open_fs.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:200], fs_array[0:200])
      return ridge
      

  def ridge_jawleft(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/jawleft_dlib.csv", delimiter=",", skiprows=1)
      #dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/jawleft_dlib_new.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/jawleft_fs.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:250], fs_array[0:250])
      return ridge
      

  def ridge_mouthleft(self):

      dlib = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/mouthleft_dlib.csv", delimiter=",", skiprows=1)
      #fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/mouthleft_only_fs.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/mouthleft_only_fs1.csv", delimiter=",", skiprows=1)
      dlib_array = numpy.array(dlib)
      fs_array = numpy.array(fs)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      ridge.fit(dlib_array[0:200], fs_array[0:200])
      return ridge
      

  def ridge_brow_model(self):
      dlib_xy = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/browsup_unnormalized1.csv", delimiter=",", skiprows=1)
      #dlib_xy = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/browsup_normalized_new.csv", delimiter=",", skiprows=1)
      fs = numpy.loadtxt('' + "/home/meareg/dlib_ws/src/dlib_puppeteering/src/fs_browsup_eyeblink.csv", delimiter=",", skiprows=1)
      dlib_xy_array = numpy.array(dlib_xy)
      fs_array = numpy.array(fs)
      #print(dlib_xy)
      
      alpha = 0.1
      ridge = Ridge(alpha = alpha)
      #ridge.fit(dlib_xy_array[0:120], fs_array[0:120])
      ridge.fit(dlib_xy_array[100:450], fs_array[100:450]) 
      #ridge.fit(dlib_xy_array[0:250], fs_array[0:250]) 
      #ridge.fit(dlib_xy_array[81:105], fs_array[0:250]) 
      #ridge.fit(dd[100:450], fs[100:450])
      #ridge.fit(dd[100:450], fs[100:450])
      #ridge.fit(ddxy[100:450], fs[100:450])
      #ridge.fit(dlib_xy_array[0:100], fs_array[0:100])
      #ridge.score(ddxy[450:595], fs[450:595])

      #ridge = Ridge(0.1)
      #ridge.fit(ddxy[0:2], fs[0:2])
      #ridge.fit(brow_sel[0:2], fs[0:2])
      #ridge._coeff = coeff_brows_up
      #ridge._coeff = coeff_brows_up_2
      #ridge._intercept = intercept_brows_up
      #ridge._coeff = coeff_brows_up_fake
      #ridge._intercept = intercept_brows_up_2
      return ridge

  def doMapping(self):
      xy_normalized = []
      x_new = []
      
      # brows up 256x256 neutral expressions of dlib points from x[17:27] to y[17:27] (points most important during brows up)
      # neutral_brows2  = ([70, 80, 93, 106, 119, 138, 150, 162, 174, 183, 90, 81, 79, 81, 85, 86, 81, 79, 81, 89])
      #neutral_brows_x = ([72, 82, 95, 108, 121, 139, 151, 163, 175, 183])
      #neutral_brows_y = ([87, 79, 76, 78, 83, 83, 78, 76, 79, 87])

      # For Browsup_normalized_new.csv (minimum (0) value at index 89)
      neutral_brows_x = ([67, 75, 87, 99, 110, 129, 140, 151, 162, 169])
      neutral_brows_y = ([84, 76, 74, 77, 81, 81, 77, 75, 78, 86])


      #max_brow_x = ([69, 76, 87, 98, 108, 128, 138, 149, 159, 165])
      #max_brow_y = ([82, 74, 72, 72, 77, 78, 74, 74, 78, 86])

      #neutral_brows_x_scaled  = ([180.0, 205.0, 237.5, 270.0, 302.5, 347.5, 377.5, 407.5, 437.5, 457.5])
      #neutral_brows_y_scaled = ([163.125, 148.125, 142.5, 146.25, 155.625, 155.625, 146.25, 142.5, 148.125, 163.125])

      #neutral_brows_scaled = ([70, 79, 93, 107, 120, 138, 150, 163, 175, 184, 90, 81, 78, 80, 85, 85, 80, 79, 81, 90])
      #neutral_mouthleft_import_landmarks  = ([X48, X49, X50, X51, X57, X58, X59, X60, X61, X62, X66, X67])
      neutral_mouthleft = ([111, 120, 130, 129, 120, 116, 129])#, 130])
      #neutral_jawleft = ([X3, X4, X5, X6, X7, X8, X9, X49, X50, X51, X52, X53, X58, X59, X60, X61])
      neutral_jawleft  = ([68, 75, 85, 97, 113, 132, 152, 116, 126, 134, 141, 149, 125, 115, 112, 125])




      #neutral_mouthleft = ([140, 150, 159, 150, 140, 132, 110, 124, 132, 140, 154, 140, 132, 124])


      
      # convert the 256x256 to its 640x480 resolution equivalent. Doing this increases the gaps between numbers which in return would be good give chance of delicate numbers being detected during prediction correctly.
      # Use the formula below for conversion:
      ''' neutral_brows_scaled_x = []
          for i in range(0, len(neutral_brows[0:10])):
              neutral_brows_scaled.append(neutral_pose_brows_up[i]*640/256)'''

      ''' neutral_brows_scaled_y = []
          for i in range(0, len(neutral_brows[10:20])):
              neutral_brows_scaled.append(neutral_pose_brows_up[i]*480/256)'''


      #neutral_brows_scaled = ([169.875, 193.46875, 224.140625, 254.8125, 285.484375, 327.953125, 356.265625, 384.578125, 412.890625, 431.765625, 205.265625, 186.390625, 179.3125, 184.03125, 195.828125, 195.828125, 184.03125, 179.3125, 186.390625, 205.265625])
      
      # Map any corresponding landmark input points (x[17:27], y[17:27]) from dlib relative to the given neutral pose landmarks on the above line.
      # sample dlib values of a single frame

      #x_brow = ([321, 332, 347, 364, 379, 408, 424, 441, 458, 472])	
      #y_brow= ([176, 165, 162, 164, 169, 168, 161, 158, 160, 171])
      #x = x/640 * 256
      #y = y/480 * 256

      x = self.dlibX[0:67]
      y = self.dlibY[0:67]

      x_brow = x[17:27]
      y_brow = y[17:27]




      x_i_jawleft = x[3:10]
      x_ii_jawleft = x[49:54]
      x_iii_jawleft = x[58:62]


      x_jawleft = x_i_jawleft + x_ii_jawleft + x_iii_jawleft
      #print('x_jawleft')
      #print(x_jawleft)

      '''x_jawleft_scaled = []

      for i in range(0, len(x_jawleft)):
          x_jawleft_scaled.append(x_jawleft[i]*256/640)
      print('x_jawleft_scaled')
      print(x_jawleft_scaled)


      x_jawleft_modified = []
      for i in range(0, len(x_jawleft)):
          x_jawleft_modified.append(100*(x_jawleft_scaled[8] - x_jawleft_scaled[i])/(x_jawleft_scaled[8] - x_jawleft_scaled[0]))

      x_jawleft_numpy = numpy.array(x_jawleft_modified)
      ridge_jawleft = self.ridge_jawleft()
      predicted_jawleft = ridge_jawleft.predict(x_jawleft_numpy)
      print('x_jawleft_modified')
      print(x_jawleft_modified)
      print('predicted_jawleft')
      print(predicted_jawleft)'''

      x_jawleft_scaled = []

      for i in range(0, len(x_jawleft)):
          x_jawleft_scaled.append(x_jawleft[i]*256/640)
      print('x_jawleft_scaled')
      #print(x_jawleft_scaled)

      x_jawleft_new = [neutral_jawleft[0], neutral_jawleft[1]]
      #x_jawleft_new=[]

      for i in range(2, len(x_jawleft)):
          x_jawleft_new.append(x_jawleft_new[i-1] + ((x_jawleft_scaled[i] - x_jawleft_scaled[i-1]) * (neutral_jawleft[i-1] - neutral_jawleft[0])/(x_jawleft_scaled[i-1] - x_jawleft_scaled[0])))

      #print('x_jawleft_new')
      #print(x_jawleft_new)


      x_jawleft_numpy = numpy.array(x_jawleft_new)
      ##ridge_jawleft = self.ridge_jawleft()
      ##predicted_jawleft = ridge_jawleft.predict(x_jawleft_numpy)
      #print('predicted_jawleft')
      #print(predicted_jawleft)



      x_i_mouthleft = x[48:51]
      x_ii_mouthleft = x[58:62]
      #x_iii_mouthleft = x[67]

      x_mouthleft = x_i_mouthleft + x_ii_mouthleft# + x_iii_mouthleft
      #print('x_mouthleft')
      #print(x_mouthleft)

      x_mouthleft_scaled = []

      for i in range(0, len(x_mouthleft)):
          x_mouthleft_scaled.append(x_mouthleft[i]*256/640)
      #print('x_mouthleft_scaled')
      #print(x_mouthleft_scaled)

      x_mouthleft_new = [neutral_mouthleft[0], neutral_mouthleft[1]]

      for i in range(2, len(x_mouthleft)):
          x_mouthleft_new.append(x_mouthleft_new[0] + ((x_mouthleft_scaled[i] - x_mouthleft_scaled[0]) * (neutral_mouthleft[i-1] - neutral_mouthleft[0])/(x_mouthleft_scaled[i-1] - x_mouthleft_scaled[0])))

      #print('x_mouthleft_new')
      #print(x_mouthleft_new)



      x_mouthleft_numpy = numpy.array(x_mouthleft_new)
      ridge_mouthleft = self.ridge_mouthleft()
      predicted_mouthleft = ridge_mouthleft.predict(x_mouthleft_numpy)
      #print('predicted_mouthleft')
      #print(predicted_mouthleft)
      #print(x_mouthleft_new)


      x_brow_scaled = []
      y_brow_scaled = []

      for i in range(0, len(x_brow)):
          x_brow_scaled.append(x_brow[i]*256/640)
      for i in range(0, len(y_brow)):
          y_brow_scaled.append(y_brow[i]*256/480)

      x_brow = x_brow_scaled
      y_brow = y_brow_scaled

      x_neutral = neutral_brows_x[0:10]
      y_neutral = neutral_brows_y[0:10]

      #x_neutral = neutral_brows_scaled[0:10]
      #y_neutral = neutral_brows_scaled[10:20]
      print('brow_dlib')
      print(x_brow + y_brow)
      print('x[0] and x[16]')
      print(x[0])
      print(x[16])
      print('y[0] and y[16]')
      print(y[0])
      print(y[16])
      x16 = x[16]*256/640
      x0 = x[0]*256/640
      print(x16)
      print(x0)
      y16 = y[16]*256/480
      y0 = y[0]*256/480
      print(y16-y0)
      #print(y0)

      '''x_brow_new = [x_neutral[0], x_neutral[1]]
      #x_brow_new.append(x_neutral[0] + (x_neutral[1] - x_neutral[0]))

      y_brow_new = [y_neutral[0], y_neutral[1]]
      #y_brow_new.append(y_neutral[0] + (y_neutral[1] - y_neutral[0]))'''

      x_brow_new = [x_neutral[0]]
      y_brow_new = [y_neutral[0]] 
      x16 = x[16]*256/640
      x0 = x[0]*256/640
      factor = ((174-57) / (x16 - x0)) # columns x[16] and x[0] of neutral value (0) browsup of 256 x 256 index 89.


      for i in range(1, len(x_brow)):
          x_brow_new.append(x_brow_new[i-1] + ((x_brow[i] - x_brow[i-1]) * factor))

      for i in range(1, len(y_brow)):
          y_brow_new.append(y_brow_new[i-1] + ((y_brow[i] - y_brow[i-1]) * factor))

      factor_brow_neutral = 101-98 # columns y[16] and y[0] of neutral value (0) browsup of 256 x 256 index 89.
      factor_brow_y = y16 - y0  
      total_factor = factor_brow_neutral - factor_brow_y 
      
      y_brow_newer = []   
      
      for i in range(0, len(y_brow_new)):
          y_brow_newer.append(y_brow_new[i] - total_factor)
          #total_factor = total_factor-(total_factor/4)

      '''total_factor = factor_brow_neutral + factor_brow_y
      for i in range(9, 4, --1):
          y_brow_newer.append(y_brow_new[i] + total_factor)
          total_factor = total_factor/2'''



      '''for i in range(2, len(y_brow)):
             x_brow_new.append(x_brow_new[0] + ((y_brow[i] - y_brow[0]) * (y_neutral[i-1] - y_neutral[0])/(x_brow[i-1] - x_brow[0])))

      for i in range(2, len(y_brow)):
          if y_brow[i-1] - y_brow[0] == 0:
              y_brow_new.append(y_brow_new[i-1] + (((y_brow[i] - y_brow[i-1]) * (y_neutral[i-1] - y_neutral[0]))/(y_brow[i-1] - y_brow[0]+1)))
          else:
              y_brow_new.append(y_brow_new[i-1] + (((y_brow[i] - y_brow[i-1]) * (y_neutral[i-1] - y_neutral[0]))/(y_brow[i-1] - y_brow[0])))'''

      '''for i in range(2, len(x_brow)):
          x_brow_new.append(x_brow_new[i-1] + (((x_brow[i] - x_brow[i-1]) * (x_neutral[1] - x_neutral[0]))/(x_brow[1] - x_brow[0])))

      for i in range(2, len(y_brow)):
          if y_brow[i-1] - y_brow[0] == 0:
              y_brow_new.append(y_brow_new[i-1] + ((y_brow[i] - y_brow[i-1]) * (y_neutral[i-1] - y_neutral[0])/(y_brow[1] - y_brow[0]+1)))
          else:
              y_brow_new.append(y_brow_new[i-1] + ((y_brow[i] - y_brow[i-1]) * (y_neutral[i-1] - y_neutral[0])/(y_brow[1] - y_brow[0])))'''


      '''x_brow_new = [x_neutral[0]]


      y_brow_new = [y_neutral[0]]

      for i in range(1, len(x_brow)):
          x_brow_new.append((x_neutral[0] * x_brow[i]) / x_brow[0])


      for i in range(1, len(y_brow)):
          if y_brow[i] - y_brow[0] == 0:
              y_brow_new.append((y_neutral[0] * y_brow[i]) / y_brow[0]+1)
          else:
              y_brow_new.append((y_neutral[0] * y_brow[i]) / y_brow[0])'''

      #to be fed to the ridge model
      xy_brow_new = x_brow_new + y_brow_newer

      print('xy_brow_new')
      print(xy_brow_new)
      print('y_brow_newer')
      print(y_brow_newer)

      brow_numpy = numpy.array(xy_brow_new)
      ridge_brow = self.ridge_brow_model()
      predicted_brow = ridge_brow.predict(brow_numpy)
      #predicted_brow = predicted_brow
      print('predicted_brow')
      print(predicted_brow)
      '''if self.once == 0:
          self.once = 1
          self.ridge = self.ridge_model()
          predicted_brow  = self.ridge.predict(ddxy[0:100])
          predicted_brow  = self.ridge.predict(ddxy[450:590])
          print(predicted_brow)
          print(predicted_brow)'''
      #else:
      #predicted_shapekey = ridge.predict(xy_normalized)

      # predict lowerlip open 
      #y_lowerlipdown_open_i = y[54:60]
      #y_lowerlipdown_open_ii = y[63:67]

      # y_lowerlipdown_open_neutral = [177, 184, 187, 187, 186, 182, 177, 174, 175, 173]
      y_lowerlipdown_open_i = y[55:60]
      y_lowerlipdown_open_ii = y[65:67]
      y_lowerlipdown_open_neutral = [184, 187, 187, 186, 182, 174, 175]
  
      y_lowerlipdown_open = y_lowerlipdown_open_i + y_lowerlipdown_open_ii 


      y_lowerlipdown_open_scaled = []

      for i in range(0, len(y_lowerlipdown_open)):
          y_lowerlipdown_open_scaled.append(y_lowerlipdown_open[i]*256/480)

      y_lowerlipdown_open = y_lowerlipdown_open_scaled

      y_lowerlipdown_open_new = [y_lowerlipdown_open_neutral[0]] 

      #factor = ((210-73) / (x16 - x0)) # columns x[16] and x[0] of neutral value (0) open.csv of 256 x 256 index 8.

      factor_y_lowerlipdown_open_neutral = 112-104 # columns y[16] and y[0] of neutral value (0) open.csv of 256 x 256 index 8.
      factor_y_lowerlipdown_open = y16 - y0  
      #total_factor = factor_y_lowerlipdown_open_neutral / factor_y_lowerlipdown_open # handle division by zeros


      for i in range(1, len(y_lowerlipdown_open)):
          y_lowerlipdown_open_new.append(y_lowerlipdown_open_new[i-1] + ((y_lowerlipdown_open[i] - y_lowerlipdown_open[i-1])))#* total_factor))
      '''for i in range(1, len(y_lowerlipdown_open)):
          y_lowerlipdown_open_new.append(y_lowerlipdown_open_neutral[i-1] + ((y_lowerlipdown_open_scaled[i] - y_lowerlipdown_open_scaled[i-1]) * total_factor))'''


      

      '''y_lowerlipdown_open_newer = []
      for i in range(0, len(y_lowerlipdown_open_new)):
          y_lowerlipdown_open_newer.append(y_lowerlipdown_open_new[i] - total_factor)'''



      # enter normalization code here

      #lowerlipdown_numpy = numpy.array(y_lowerlipdown_open_newer)
      '''lowerlipdown_numpy = numpy.array(y_lowerlipdown_open_new)

      ridge_lowerlipdown = self.ridge_openlowerlip()
      predicted_lowerlipdown = ridge_lowerlipdown.predict(lowerlipdown_numpy)
      print('predicted_lowerlipdown')
      print(predicted_lowerlipdown)'''






      x_i_leftsmile = x[51:58]
      x_ii_leftsmile = x[62:67]
      y_i_leftsmile = y[51:58]
      y_ii_leftsmile = y[62:67]
      x_leftsmile =  x_i_leftsmile + x_ii_leftsmile 
      y_leftsmile =  y_i_leftsmile + y_ii_leftsmile 

      x_leftsmile_scaled = []
      y_leftsmile_scaled = []

      for i in range(0, len(x_leftsmile)):
          x_leftsmile_scaled.append(x_leftsmile[i]*256/640)
      for i in range(0, len(y_leftsmile)):
          y_leftsmile_scaled.append(y_leftsmile[i]*256/480)


      #x_leftsmile = x_leftsmile_scaled
      #y_leftsmile = y_leftsmile_scaled

      neutral_leftsmile_x = ([126, 133, 141, 150, 142, 134, 126, 126, 133, 147, 133, 126]) 
      neutral_leftsmile_y = ([168, 165, 167, 171, 179, 183, 183, 173, 172, 171, 172, 173])

      x_leftsmile_new = [neutral_leftsmile_x[0]]
      y_leftsmile_new = [neutral_leftsmile_y[0]] 
      '''x66 = x[66]*256/640
      x51 = x[51]*256/640
   
      factor = ((126-126) / (x66 - x51)) # columns x[16] and x[0] of neutral value (0)  left of 256 x 256 index 3.
      
      y66 = y[66]*256/480
      y51 = y[51]*256/480

      factor = ((126-126)/ (y66 - y51)) # columns x[16] and x[0] of neutral value (0)  left of 256 x 256 index 3.'''
   
      #y66 = y[66]*256/480
      #y51 = y[51]*256/480
      factor_smileleft_y = ((107-110) / (y[66] - y[51])) # columns y[16] and y[0] of neutral value (0)  left of 256 x 256 smile.csv index 0.'''
   

      for i in range(1, len(x_leftsmile)):
          x_leftsmile_new.append(x_leftsmile_new[i-1] + ((x_leftsmile[i] - x_leftsmile[i-1])))# * factor))

      for i in range(1, len(y_leftsmile)):
          y_leftsmile_new.append(y_leftsmile_new[i-1] + ((y_leftsmile[i] - y_leftsmile[i-1]) * factor))



      xy_leftsmile_new = x_leftsmile_new + y_leftsmile_new

      print('xy_leftsmile_new')
      print(xy_leftsmile_new)

      print('y_leftsmile_new')
      print(y_leftsmile_new)

      ##leftsmile_numpy = numpy.array(xy_leftsmile_new)
      ##print('leftsmile_numpy')
      ##print(leftsmile_numpy)  
      ##ridge_leftsmile = self.ridge_leftsmile()
      ##predicted_leftsmile = ridge_leftsmile.predict(leftsmile_numpy)
      ##print('predicted_leftsmile')
      ##print(predicted_leftsmile)

      x_smile_left_new = x[48:52]

      #new leftsmile prediction 
      neutral_smile_new_left = ([102, 111, 119, 126])

      x_smile_new_left_scaled = []

      for i in range(0, len(x_smile_left_new)):
          x_smile_new_left_scaled.append(x_smile_left_new[i]*256/640)

      
      x_smile_left  = x_smile_new_left_scaled


      x_smile_new = [neutral_smile_new_left[0]]


      # factor x16 changed to 230 from 183; for better result (experimental)
      factor_smile_x_new = ((230-62) / (x16 - x0+1)) # 183 and 62 are columns x[16] and x[0] of neutral value (0) smile.csv of 256 x 256 index 2 respectively.


      for i in range(1, len(x_smile_left_new)):
          x_smile_new.append(x_smile_new[i-1] + ((x_smile_left[i] - x_smile_left[i-1]) * factor_smile_x_new))


      #factor_smile = abs(factor_smile_neutral - factor_smile_y)
      '''factor_smile_total_y = factor_smile_neutral_y - factor_smile_y 

      for i in range(1, len(smile_right_y)):
          y_smile_new.append((y_smile_new[i-1] + ((smile_right_y[i] - smile_right_y[i-1]) * factor_smile_x)) - factor_smile_total_y)'''


      #xy_smile_numpy = numpy.array(x_smile_new + y_smile_new)
      x_smile_numpy = numpy.array(x_smile_new)
      leftsmile = self.ridge_leftsmile()
      predicted_smileleft = leftsmile.predict(x_smile_numpy)
      print("predicted_smileleft")
      print(predicted_smileleft)







      neutral_lipupperleft_m_x = ([122, 128, 135, 142, 122, 128, 139])
      neutral_lipupperleft_m_y = ([172, 170, 171, 174, 176, 175, 175])

      x_lipupperleft_m_new = [neutral_lipupperleft_m_x[0]]
      y_lipupperleft_m_new = [neutral_lipupperleft_m_y[0]]

      x_i_lipupperleft_m = x[51:55]
      x_ii_lipupperleft_m  = x[62:65]
      y_i_lipupperleft_m = y[51:55]
      y_ii_lipupperleft_m  = y[62:65]

      x_lipupperleft_m =  x_i_lipupperleft_m + x_ii_lipupperleft_m 
      y_lipupperleft_m =  y_i_lipupperleft_m + y_ii_lipupperleft_m

      x_lipupperleft_m_scaled = []
      y_lipupperleft_m_scaled = []

      for i in range(0, len(x_lipupperleft_m)):
          x_lipupperleft_m_scaled.append(x_lipupperleft_m[i]*256/640)
      for i in range(0, len(y_lipupperleft_m)):
          y_lipupperleft_m_scaled.append(y_lipupperleft_m[i]*256/480)

      
      x_lipupperleft_m  = x_lipupperleft_m_scaled
      y_lipupperleft_m =  y_lipupperleft_m_scaled


 
      '''factor_x = ((175-172) / (y[64] - y[51])) 
      factor_y = ((139-122) / (x[64] - x[51]))''' 

      for i in range(1, len(x_lipupperleft_m)):
          x_lipupperleft_m_new.append(x_lipupperleft_m_new[i-1] + ((x_lipupperleft_m[i] - x_lipupperleft_m[i-1]))) #* factor_x))

      for i in range(1, len(y_lipupperleft_m)):
          y_lipupperleft_m_new.append(y_lipupperleft_m_new[i-1] + ((y_lipupperleft_m[i] - y_lipupperleft_m[i-1])))  #* factor_y))



      xy_lipupperleft_m_new = x_lipupperleft_m_new + y_lipupperleft_m_new


      lipupperleft_numpy = numpy.array(xy_lipupperleft_m_new)
      ridge_lipupperleft = self.ridge_lipupperleft()
      predicted_lipupperleft = ridge_lipupperleft.predict(lipupperleft_numpy)
      print('predicted_lipupperleft')
      print(predicted_lipupperleft)

      smile_right_neutral_x  = ([126, 133, 141, 150])
      #smile_right_neutral_x  = ([126, 133, 141, 150, 142, 134, 126, 126, 133, 146, 133, 126])
      smile_right_neutral_y = ([168, 165, 167, 171, 179, 183, 183, 173, 172, 171, 172, 173])




      #smile_right_x_i = x[51:58]
      #smile_right_x_ii = x[62:67]
      smile_right_x = x[51:55]
      #smile_right_x = smile_right_x_i + smile_right_x_ii
      x_smile_new = [smile_right_neutral_x[0]] 

      #smile_right_y_i = y[51:58]
      #smile_right_y_ii = y[62:67]
      #smile_right_y = smile_right_y_i + smile_right_y_ii
      #y_smile_new = [smile_right_neutral_y[0]] 



      '''neutral_smile_scaled = []
      for i in range(0, len(smile_right_neutral_x )):
          neutral_smile_scaled.append(smile_right_neutral_x [i])'''

      x_smile_scaled = []
      for i in range(0, len(smile_right_x)):
          x_smile_scaled.append(smile_right_x[i]*256/640)

      smile_right_x =  x_smile_scaled

      #print('neutral_smile_scaled')
      #print(neutral_smile_scaled)

      print('x_smile scaled')
      print(x_smile_scaled)
      print(x16)
      print(x0)

      '''y_smile_scaled = []
      for i in range(0, len(smile_right_y)):
          y_smile_scaled.append(smile_right_y[i]*256/480)

      smile_right_y =  y_smile_scaled
     
      factor_smile_neutral_y = 106-109
      factor_smile_y = y16 - y0 '''

      # factor of x is changed from the 183 to 210; just for experiment
      factor_smile_x = ((200-63) / (x16 - x0+1)) # 200 and 63 are columns x[16] and x[0] of neutral value (0) smile_new1.csv of 256 x 256 index 4 respectively.

      factor_smile_y = (106-109) / (y16 - y0) # 106 and 109 are columns y[16] and y[0] of neutral value (0) smile_new1.csv of 256 x 256 index 4 respectively.


      for i in range(1, len(smile_right_x)):
          x_smile_new.append(x_smile_new[i-1] + ((smile_right_x[i] - smile_right_x[i-1]) * factor_smile_x))


      #factor_smile = abs(factor_smile_neutral - factor_smile_y)
      '''factor_smile_total_y = factor_smile_neutral_y - factor_smile_y 

      for i in range(1, len(smile_right_y)):
          y_smile_new.append((y_smile_new[i-1] + ((smile_right_y[i] - smile_right_y[i-1]) * factor_smile_x)) - factor_smile_total_y)'''


      #xy_smile_numpy = numpy.array(x_smile_new + y_smile_new)
      x_smile_numpy = numpy.array(x_smile_new)
      rightsmile = self.ridge_rightsmile()
      predicted_smileright = rightsmile.predict(x_smile_numpy)
      print('predicted_smileright')
      print(predicted_smileright)
      print('smile points')
      print(x_smile_new)




      '''factor_brow_neutral = 101-98 # columns y[16] and y[0] of neutral value (0) browsup of 256 x 256 index 89.
      factor_brow_y = y16 - y0  
      total_factor = factor_brow_neutral - factor_brow_y 
      
      y_brow_newer = []   
      
      for i in range(0, len(y_brow_new)):
          y_brow_newer.append(y_brow_new[i] - total_factor)
          #total_factor = total_factor-(total_factor/4)'''



      '''factor_brow_neutral = 101-98 # columns y[16] and y[0] of neutral value (0) browsup of 256 x 256 index 89.
      factor_brow_y = y16 - y0  
      total_factor = factor_brow_neutral - factor_brow_y 
      
      y_brow_newer = []   
      
      for i in range(0, len(y_brow_new)):
          y_brow_newer.append(y_brow_new[i] - total_factor)
          #total_factor = total_factor-(total_factor/4)'''


      blendshape_values = []
      for i in range(0, 45): # modify this block to include the machine learning approach
          if i in self.indexes_brow:
              #random_val= random.random() # generate some random values between 0 and 1
              #blendshape_values.append(random_val)
              blendshape_values.append(predicted_brow) 
              #print('random on print')
          #if i in self.indexes_mouth:
              #x = 0
              #random_val= random.random() # generate some random values between 0 and 1
              #blendshape_values.append(random_val)
              #blendshape_values.append(0.4)
              #blendshape_values.append(predicted_mouthleft)
              #blendshape_values.append(predicted_jawleft)


              #print(self.blendshape_names[i])
          #if i in self.indexes_lowerlipdown:
          #    blendshape_values.append(predicted_lowerlipdown)
          if i in self.indexes_smileleft:
              blendshape_values.append(predicted_smileright)
              #blendshape_values.append(predicted_smileright)
          if i in self.indexes_smileright:
              blendshape_values.append(predicted_smileright)
          if i in self.indexes_lipupperleft:
              #blendshape_values.append(predicted_jawleft)
              #blendshape_values.append(predicted_lipupperleft)
              blendshape_values.append(predicted_smileright/1.3)


          else:
              blendshape_values.append(0.0)
          #if i == 44:
          #    i = 0
      #print(blendshape_values)
      return blendshape_values

def main(args):
  rospy.init_node('dlib2blender_mapper', anonymous=True)
  dlib_puppeteering()
  try:
      rospy.spin()
  except KeyboardInterrupt:
      print("Dlib-Puppeteering Exiting...")
  #cv2.destroyAllWindows()

if __name__ == '__main__':
  #print('hello')
  main(sys.argv)







