;; Auto-generated. Do not edit!


(when (boundp 'ogretici_paket::Batarya_Durum)
  (if (not (find-package "OGRETICI_PAKET"))
    (make-package "OGRETICI_PAKET"))
  (shadow 'Batarya_Durum (find-package "OGRETICI_PAKET")))
(unless (find-package "OGRETICI_PAKET::BATARYA_DURUM")
  (make-package "OGRETICI_PAKET::BATARYA_DURUM"))

(in-package "ROS")
;;//! \htmlinclude Batarya_Durum.msg.html


(defclass ogretici_paket::Batarya_Durum
  :super ros::object
  :slots (_batarya ))

(defmethod ogretici_paket::Batarya_Durum
  (:init
   (&key
    ((:batarya __batarya) "")
    )
   (send-super :init)
   (setq _batarya (string __batarya))
   self)
  (:batarya
   (&optional __batarya)
   (if __batarya (setq _batarya __batarya)) _batarya)
  (:serialization-length
   ()
   (+
    ;; string _batarya
    4 (length _batarya)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _batarya
       (write-long (length _batarya) s) (princ _batarya s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _batarya
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _batarya (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get ogretici_paket::Batarya_Durum :md5sum-) "cf2f5dfec1a5a686917c26b6ec537920")
(setf (get ogretici_paket::Batarya_Durum :datatype-) "ogretici_paket/Batarya_Durum")
(setf (get ogretici_paket::Batarya_Durum :definition-)
      "string batarya

")



(provide :ogretici_paket/Batarya_Durum "cf2f5dfec1a5a686917c26b6ec537920")


