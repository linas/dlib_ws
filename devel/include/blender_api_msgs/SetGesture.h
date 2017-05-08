// Generated by gencpp from file blender_api_msgs/SetGesture.msg
// DO NOT EDIT!


#ifndef BLENDER_API_MSGS_MESSAGE_SETGESTURE_H
#define BLENDER_API_MSGS_MESSAGE_SETGESTURE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace blender_api_msgs
{
template <class ContainerAllocator>
struct SetGesture_
{
  typedef SetGesture_<ContainerAllocator> Type;

  SetGesture_()
    : name()
    , repeat(0)
    , speed(0.0)
    , magnitude(0.0)  {
    }
  SetGesture_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , repeat(0)
    , speed(0.0)
    , magnitude(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef int32_t _repeat_type;
  _repeat_type repeat;

   typedef float _speed_type;
  _speed_type speed;

   typedef float _magnitude_type;
  _magnitude_type magnitude;




  typedef boost::shared_ptr< ::blender_api_msgs::SetGesture_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::blender_api_msgs::SetGesture_<ContainerAllocator> const> ConstPtr;

}; // struct SetGesture_

typedef ::blender_api_msgs::SetGesture_<std::allocator<void> > SetGesture;

typedef boost::shared_ptr< ::blender_api_msgs::SetGesture > SetGesturePtr;
typedef boost::shared_ptr< ::blender_api_msgs::SetGesture const> SetGestureConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::blender_api_msgs::SetGesture_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::blender_api_msgs::SetGesture_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace blender_api_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'blender_api_msgs': ['/home/esku/dlib_ws/src/blender_api_msgs/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::blender_api_msgs::SetGesture_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::SetGesture_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::SetGesture_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9ee7a070659b1ce3345274c40a2a881d";
  }

  static const char* value(const ::blender_api_msgs::SetGesture_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9ee7a070659b1ce3ULL;
  static const uint64_t static_value2 = 0x345274c40a2a881dULL;
};

template<class ContainerAllocator>
struct DataType< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
{
  static const char* value()
  {
    return "blender_api_msgs/SetGesture";
  }

  static const char* value(const ::blender_api_msgs::SetGesture_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n\
int32 repeat\n\
float32 speed\n\
float32 magnitude\n\
";
  }

  static const char* value(const ::blender_api_msgs::SetGesture_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.repeat);
      stream.next(m.speed);
      stream.next(m.magnitude);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetGesture_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::blender_api_msgs::SetGesture_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::blender_api_msgs::SetGesture_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "repeat: ";
    Printer<int32_t>::stream(s, indent + "  ", v.repeat);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
    s << indent << "magnitude: ";
    Printer<float>::stream(s, indent + "  ", v.magnitude);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLENDER_API_MSGS_MESSAGE_SETGESTURE_H