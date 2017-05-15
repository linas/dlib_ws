// Generated by gencpp from file pau2motors/pau.msg
// DO NOT EDIT!


#ifndef PAU2MOTORS_MESSAGE_PAU_H
#define PAU2MOTORS_MESSAGE_PAU_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Quaternion.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Quaternion.h>

namespace pau2motors
{
template <class ContainerAllocator>
struct pau_
{
  typedef pau_<ContainerAllocator> Type;

  pau_()
    : m_headRotation()
    , m_headTranslation()
    , m_neckRotation()
    , m_eyeGazeLeftPitch(0.0)
    , m_eyeGazeLeftYaw(0.0)
    , m_eyeGazeRightPitch(0.0)
    , m_eyeGazeRightYaw(0.0)
    , m_coeffs()
    , m_shapekeys()  {
    }
  pau_(const ContainerAllocator& _alloc)
    : m_headRotation(_alloc)
    , m_headTranslation(_alloc)
    , m_neckRotation(_alloc)
    , m_eyeGazeLeftPitch(0.0)
    , m_eyeGazeLeftYaw(0.0)
    , m_eyeGazeRightPitch(0.0)
    , m_eyeGazeRightYaw(0.0)
    , m_coeffs(_alloc)
    , m_shapekeys(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Quaternion_<ContainerAllocator>  _m_headRotation_type;
  _m_headRotation_type m_headRotation;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _m_headTranslation_type;
  _m_headTranslation_type m_headTranslation;

   typedef  ::geometry_msgs::Quaternion_<ContainerAllocator>  _m_neckRotation_type;
  _m_neckRotation_type m_neckRotation;

   typedef float _m_eyeGazeLeftPitch_type;
  _m_eyeGazeLeftPitch_type m_eyeGazeLeftPitch;

   typedef float _m_eyeGazeLeftYaw_type;
  _m_eyeGazeLeftYaw_type m_eyeGazeLeftYaw;

   typedef float _m_eyeGazeRightPitch_type;
  _m_eyeGazeRightPitch_type m_eyeGazeRightPitch;

   typedef float _m_eyeGazeRightYaw_type;
  _m_eyeGazeRightYaw_type m_eyeGazeRightYaw;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _m_coeffs_type;
  _m_coeffs_type m_coeffs;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _m_shapekeys_type;
  _m_shapekeys_type m_shapekeys;




  typedef boost::shared_ptr< ::pau2motors::pau_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pau2motors::pau_<ContainerAllocator> const> ConstPtr;

}; // struct pau_

typedef ::pau2motors::pau_<std::allocator<void> > pau;

typedef boost::shared_ptr< ::pau2motors::pau > pauPtr;
typedef boost::shared_ptr< ::pau2motors::pau const> pauConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pau2motors::pau_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pau2motors::pau_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pau2motors

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'pau2motors': ['/home/icog-labs/dlib_ws/src/pau2motors/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pau2motors::pau_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pau2motors::pau_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pau2motors::pau_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pau2motors::pau_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pau2motors::pau_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pau2motors::pau_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pau2motors::pau_<ContainerAllocator> >
{
  static const char* value()
  {
    return "49c3e3c79051e845f49e85a5ebffa67a";
  }

  static const char* value(const ::pau2motors::pau_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x49c3e3c79051e845ULL;
  static const uint64_t static_value2 = 0xf49e85a5ebffa67aULL;
};

template<class ContainerAllocator>
struct DataType< ::pau2motors::pau_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pau2motors/pau";
  }

  static const char* value(const ::pau2motors::pau_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pau2motors::pau_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Quaternion m_headRotation\n\
geometry_msgs/Vector3    m_headTranslation\n\
geometry_msgs/Quaternion m_neckRotation\n\
\n\
float32 m_eyeGazeLeftPitch\n\
float32 m_eyeGazeLeftYaw\n\
float32 m_eyeGazeRightPitch\n\
float32 m_eyeGazeRightYaw\n\
\n\
#An array of blendshape coefficients.\n\
#They describe an expression of a virtual face.\n\
float32[] m_coeffs\n\
# Then setting shapekey values, names must be passed\n\
string[] m_shapekeys\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::pau2motors::pau_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pau2motors::pau_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.m_headRotation);
      stream.next(m.m_headTranslation);
      stream.next(m.m_neckRotation);
      stream.next(m.m_eyeGazeLeftPitch);
      stream.next(m.m_eyeGazeLeftYaw);
      stream.next(m.m_eyeGazeRightPitch);
      stream.next(m.m_eyeGazeRightYaw);
      stream.next(m.m_coeffs);
      stream.next(m.m_shapekeys);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pau_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pau2motors::pau_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pau2motors::pau_<ContainerAllocator>& v)
  {
    s << indent << "m_headRotation: ";
    s << std::endl;
    Printer< ::geometry_msgs::Quaternion_<ContainerAllocator> >::stream(s, indent + "  ", v.m_headRotation);
    s << indent << "m_headTranslation: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.m_headTranslation);
    s << indent << "m_neckRotation: ";
    s << std::endl;
    Printer< ::geometry_msgs::Quaternion_<ContainerAllocator> >::stream(s, indent + "  ", v.m_neckRotation);
    s << indent << "m_eyeGazeLeftPitch: ";
    Printer<float>::stream(s, indent + "  ", v.m_eyeGazeLeftPitch);
    s << indent << "m_eyeGazeLeftYaw: ";
    Printer<float>::stream(s, indent + "  ", v.m_eyeGazeLeftYaw);
    s << indent << "m_eyeGazeRightPitch: ";
    Printer<float>::stream(s, indent + "  ", v.m_eyeGazeRightPitch);
    s << indent << "m_eyeGazeRightYaw: ";
    Printer<float>::stream(s, indent + "  ", v.m_eyeGazeRightYaw);
    s << indent << "m_coeffs[]" << std::endl;
    for (size_t i = 0; i < v.m_coeffs.size(); ++i)
    {
      s << indent << "  m_coeffs[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.m_coeffs[i]);
    }
    s << indent << "m_shapekeys[]" << std::endl;
    for (size_t i = 0; i < v.m_shapekeys.size(); ++i)
    {
      s << indent << "  m_shapekeys[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.m_shapekeys[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAU2MOTORS_MESSAGE_PAU_H