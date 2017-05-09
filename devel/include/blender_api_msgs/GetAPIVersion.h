// Generated by gencpp from file blender_api_msgs/GetAPIVersion.msg
// DO NOT EDIT!


#ifndef BLENDER_API_MSGS_MESSAGE_GETAPIVERSION_H
#define BLENDER_API_MSGS_MESSAGE_GETAPIVERSION_H


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
struct GetAPIVersion_
{
  typedef GetAPIVersion_<ContainerAllocator> Type;

  GetAPIVersion_()
    : value(0)  {
    }
  GetAPIVersion_(const ContainerAllocator& _alloc)
    : value(0)  {
  (void)_alloc;
    }



   typedef uint8_t _value_type;
  _value_type value;




  typedef boost::shared_ptr< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> const> ConstPtr;

}; // struct GetAPIVersion_

typedef ::blender_api_msgs::GetAPIVersion_<std::allocator<void> > GetAPIVersion;

typedef boost::shared_ptr< ::blender_api_msgs::GetAPIVersion > GetAPIVersionPtr;
typedef boost::shared_ptr< ::blender_api_msgs::GetAPIVersion const> GetAPIVersionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace blender_api_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'blender_api_msgs': ['/home/esku/dlib_ws/src/blender_api_msgs/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e4da51e86d3bac963ee2bb1f41031407";
  }

  static const char* value(const ::blender_api_msgs::GetAPIVersion_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe4da51e86d3bac96ULL;
  static const uint64_t static_value2 = 0x3ee2bb1f41031407ULL;
};

template<class ContainerAllocator>
struct DataType< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "blender_api_msgs/GetAPIVersion";
  }

  static const char* value(const ::blender_api_msgs::GetAPIVersion_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 value\n\
";
  }

  static const char* value(const ::blender_api_msgs::GetAPIVersion_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetAPIVersion_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::blender_api_msgs::GetAPIVersion_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::blender_api_msgs::GetAPIVersion_<ContainerAllocator>& v)
  {
    s << indent << "value: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLENDER_API_MSGS_MESSAGE_GETAPIVERSION_H
