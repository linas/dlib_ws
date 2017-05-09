// Generated by gencpp from file blender_api_msgs/Visemes.msg
// DO NOT EDIT!


#ifndef BLENDER_API_MSGS_MESSAGE_VISEMES_H
#define BLENDER_API_MSGS_MESSAGE_VISEMES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <blender_api_msgs/Viseme.h>

namespace blender_api_msgs
{
template <class ContainerAllocator>
struct Visemes_
{
  typedef Visemes_<ContainerAllocator> Type;

  Visemes_()
    : data()  {
    }
  Visemes_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::blender_api_msgs::Viseme_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::blender_api_msgs::Viseme_<ContainerAllocator> >::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::blender_api_msgs::Visemes_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::blender_api_msgs::Visemes_<ContainerAllocator> const> ConstPtr;

}; // struct Visemes_

typedef ::blender_api_msgs::Visemes_<std::allocator<void> > Visemes;

typedef boost::shared_ptr< ::blender_api_msgs::Visemes > VisemesPtr;
typedef boost::shared_ptr< ::blender_api_msgs::Visemes const> VisemesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::blender_api_msgs::Visemes_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::blender_api_msgs::Visemes_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::blender_api_msgs::Visemes_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::blender_api_msgs::Visemes_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::Visemes_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::blender_api_msgs::Visemes_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::Visemes_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::blender_api_msgs::Visemes_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::blender_api_msgs::Visemes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9e70ce7b4191163ea9b52bbb867c3490";
  }

  static const char* value(const ::blender_api_msgs::Visemes_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9e70ce7b4191163eULL;
  static const uint64_t static_value2 = 0xa9b52bbb867c3490ULL;
};

template<class ContainerAllocator>
struct DataType< ::blender_api_msgs::Visemes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "blender_api_msgs/Visemes";
  }

  static const char* value(const ::blender_api_msgs::Visemes_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::blender_api_msgs::Visemes_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Viseme[] data\n\
\n\
================================================================================\n\
MSG: blender_api_msgs/Viseme\n\
string name\n\
time start\n\
duration duration\n\
float32 rampin\n\
float32 rampout\n\
float32 magnitude\n\
";
  }

  static const char* value(const ::blender_api_msgs::Visemes_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::blender_api_msgs::Visemes_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Visemes_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::blender_api_msgs::Visemes_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::blender_api_msgs::Visemes_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::blender_api_msgs::Viseme_<ContainerAllocator> >::stream(s, indent + "    ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLENDER_API_MSGS_MESSAGE_VISEMES_H
