import tempfile # libreria de un archivo temporal
import pydicom as pm # libreria que permite modificar el DICOM  

path_to_dicom = "C:/Users/Jhon/Downloads/imagen2.dcm" #Ruta y nombre de la imagen que tienes  

archivo_dicom = pm.dcmread(path_to_dicom)

# Imprimir el PatientID original
#print("PatientID original:", archivo_dicom.data_element("PatientID"))

# Imprimir información antes de la modificación
print("Antes de la modificación:") #before to modification print a name 
for de in ['PatientID', 'PatientBirthDate',"patientName" ]:
    print(de, ":", archivo_dicom.data_element(de))

# Modificar el PatientID y la fecha de nacimiento
tag_patient_id = 'PatientID'
tag_patient_name= "PatientName"
tag_birth_date = 'PatientBirthDate'



if tag_patient_id in archivo_dicom:
    archivo_dicom.data_element(tag_patient_id).value = "12345"

if tag_birth_date in archivo_dicom:
    archivo_dicom.data_element(tag_birth_date).value = "19980313"

if tag_patient_name in archivo_dicom:
    archivo_dicom.data_element(tag_patient_name).value = "jhon physics"

# Imprimir información después de la modificación
print("\nDespués de la modificación:")
for de in ['PatientID', 'PatientBirthDate']:
    print(de, ":", archivo_dicom.data_element(de))

# Guardar el archivo DICOM modificado the save the DICOM
output_filename = tempfile.NamedTemporaryFile(suffix=".dcm").name
archivo_dicom.save_as(output_filename)

print("\nArchivo DICOM modificado guardado en:", output_filename)
