// Auto-generated. Do not edit!

// (in-package ogretici_paket.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Batarya_Durum {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.batarya = null;
    }
    else {
      if (initObj.hasOwnProperty('batarya')) {
        this.batarya = initObj.batarya
      }
      else {
        this.batarya = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Batarya_Durum
    // Serialize message field [batarya]
    bufferOffset = _serializer.string(obj.batarya, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Batarya_Durum
    let len;
    let data = new Batarya_Durum(null);
    // Deserialize message field [batarya]
    data.batarya = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.batarya);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ogretici_paket/Batarya_Durum';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cf2f5dfec1a5a686917c26b6ec537920';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string batarya
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Batarya_Durum(null);
    if (msg.batarya !== undefined) {
      resolved.batarya = msg.batarya;
    }
    else {
      resolved.batarya = ''
    }

    return resolved;
    }
};

module.exports = Batarya_Durum;
