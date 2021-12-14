from flask import Flask , request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@127.0.0.1:33306/proyecto_sas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Ciudadano(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    
    departamento = db.Column(db.String(255))
    municipio = db.Column(db.String(255))
    barrio = db.Column(db.String(255))
    estrato = db.Column(db.Integer)

    nombre = db.Column(db.String(255))
    numero_documento=db.Column(db.String(255))
    fecha_nacimiento=db.Column(db.Date)    
    sexo =db.Column(db.String(1))
    telefono =db.Column(db.String(10)) 
    nivel_educativo=db.Column(db.String(255))
    ocupacion=db.Column(db.String(255))
    tipo_vivienda=db.Column(db.String(255))
    hogar_electrodomesticos=db.Column(db.Boolean)
    servicios_publicos= db.Column(db.Boolean)
    numero_personas = db.Column(db.Integer)
    ingresos_hogar=db.Column(db.Float)
    gastos_hogar=db.Column(db.Float)


    def __init__(self,departamento, municipio, barrio, estrato, nombre,numero_documento,fecha_nacimiento,sexo,telefono,nivel_educativo,ocupacion,tipo_vivienda,
    hogar_electrodomesticos,servicios_publicos,numero_personas,ingresos_hogar,gastos_hogar):
        self.departamento=departamento
        self.municipio=municipio
        self.barrio=barrio
        self.estrato=estrato

        self.nombre=nombre
        self.numero_documento=numero_documento
        self.fecha_nacimiento=fecha_nacimiento
        self.sexo=sexo
        self.telefono=telefono
        self.nivel_educativo=nivel_educativo
        self.ocupacion=ocupacion
        self.tipo_vivienda=tipo_vivienda
        self.hogar_electrodomesticos=hogar_electrodomesticos
        self.servicios_publicos=servicios_publicos
        self.numero_personas=numero_personas
        self.ingresos_hogar=ingresos_hogar
        self.gastos_hogar=gastos_hogar


db.create_all()

class CiudadanoSchema(ma.Schema):
    class Meta:
        fields=('id','departamento', 'municipio',' barrio', 'estrato', 'nombre','numero_documento','fecha_nacimiento','sexo','telefono',
        'nivel_educativo','ocupacion','tipo_vivienda','hogar_electrodomesticos','servicios_publicos','numero_personas','ingresos_hogar','gastos_hogar')

ciudadano_schema=CiudadanoSchema()
ciudadanos_schema=CiudadanoSchema(many=True)


@app.route('/ciudadanos',methods=['POST'])
def create_ciudadano():

    departamento=request.json['departamento']
    municipio=request.json['municipio']
    barrio=request.json['barrio']
    estrato=request.json['estrato']

    nombre=request.json['nombre']
    numero_documento=request.json['numero_documento']
    fecha_nacimiento=request.json['fecha_nacimiento']
    sexo=request.json['sexo']
    telefono=request.json['telefono']  
    nivel_educativo=request.json['nivel_educativo'] 
    ocupacion=request.json['ocupacion'] 
    tipo_vivienda=request.json['tipo_vivienda'] 
    hogar_electrodomesticos=request.json['hogar_electrodomesticos'] 
    servicios_publicos=request.json['servicios_publicos'] 
    numero_personas=request.json['numero_personas']   
    ingresos_hogar=request.json['ingresos_hogar'] 
    gastos_hogar=request.json['gastos_hogar'] 

    new_ciudadano = Ciudadano(departamento,municipio,barrio,estrato ,nombre,numero_documento,
    fecha_nacimiento,sexo,telefono,nivel_educativo,ocupacion,tipo_vivienda,hogar_electrodomesticos,servicios_publicos,
    numero_documento,ingresos_hogar,gastos_hogar)

    db.session.add(new_ciudadano)
    db.session.commit()

    return ciudadano_schema.jsonify(new_ciudadano)
    
@app.route('/ciudadanos',methods=['GET'])
def get_ciudadanos():
    all_ciudadanos=Ciudadano.query.all()
    resultado=ciudadanos_schema.dump(all_ciudadanos)
    return jsonify(resultado)


@app.route('/ciudadanos/<id>',methods=['GET'])
def get_ciudadano(id):
    ciudadano=Ciudadano.query.get(id)
    return ciudadano_schema.jsonify(ciudadano)


@app.route('/ciudadanos/<id>',methods=['PUT'])
def update_ciudadano(id):
    ciudadano=Ciudadano.query.get(id)

    departamento=request.json['departamento']
    municipio=request.json['municipio']
    barrio=request.json['barrio']
    estrato=request.json['estrato']

    nombre=request.json['nombre']
    numero_documento=request.json['numero_documento']
    fecha_nacimiento=request.json['fecha_nacimiento']
    sexo=request.json['sexo']
    telefono=request.json['telefono']  
    nivel_educativo=request.json['nivel_educativo'] 
    ocupacion=request.json['ocupacion'] 
    tipo_vivienda=request.json['tipo_vivienda'] 
    hogar_electrodomesticos=request.json['hogar_electrodomesticos'] 
    servicios_publicos=request.json['servicios_publicos'] 
    numero_personas=request.json['numero_personas']   
    ingresos_hogar=request.json['ingresos_hogar'] 
    gastos_hogar=request.json['gastos_hogar']

    ciudadano.departamento=departamento
    ciudadano.municipio=municipio
    ciudadano.barrio=barrio
    ciudadano.estrato=estrato

    ciudadano.nombre=nombre
    ciudadano.numero_documento=numero_documento
    ciudadano.fecha_nacimiento=fecha_nacimiento
    ciudadano.sexo=sexo
    ciudadano.telefono=telefono
    ciudadano.nivel_educativo=nivel_educativo
    ciudadano.ocupacion=ocupacion
    ciudadano.tipo_vivienda=tipo_vivienda
    ciudadano.hogar_electrodomesticos=hogar_electrodomesticos
    ciudadano.servicios_publicos=servicios_publicos
    ciudadano.numero_personas=numero_personas
    ciudadano.ingresos_hogar=ingresos_hogar
    ciudadano.gastos_hogar=gastos_hogar

    db.session.commit()  
    return ciudadano_schema.jsonify(ciudadano) 


@app.route('/ciudadanos/<id>',methods=['DELETE'])   
def delete_diudadano(id):
    ciudadano=Ciudadano.query.get(id)
    db.session.delete(ciudadano) 
    db.session.commit()

    return jsonify({'message':'El ciudadano con el id ' + id + ' fue eliminado correctamente'})


@app.route('/',methods=['GET'])
def index():
    return jsonify({'message':'Flask - Mariadb - Docker - SaS'})

if __name__ =="__main__":
    app.run(debug=True)