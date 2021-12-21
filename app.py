from flask import Flask , request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@mariadb-master:3306/clasificacion_sisben'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Ciudadano(db.Model):        
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    numero_documento=db.Column(db.String(250))
    fecha_nacimiento=db.Column(db.Date)    
    sexo =db.Column(db.String(20))
    telefono =db.Column(db.String(10)) 
    nivel_educativo=db.Column(db.String(250))
    ocupacion=db.Column(db.String(250))
    departamento = db.Column(db.String(250))
    municipio = db.Column(db.String(250))
    barrio = db.Column(db.String(250))
    estrato = db.Column(db.Integer)
    tipo_vivienda=db.Column(db.String(255))    
    servicios_publicos= db.Column(db.Boolean)
    numero_personas = db.Column(db.Integer)
    ingresos_hogar=db.Column(db.String(255))
    gastos_hogar=db.Column(db.String(255))
    clasificacion=db.Column(db.String(250))
    
    def __init__(self,nombre,numero_documento,fecha_nacimiento,sexo,telefono,nivel_educativo,ocupacion,departamento, municipio, barrio, estrato,tipo_vivienda,servicios_publicos,numero_personas,ingresos_hogar,gastos_hogar,clasificacion):
        self.nombre=nombre
        self.numero_documento=numero_documento
        self.fecha_nacimiento=fecha_nacimiento
        self.sexo=sexo
        self.telefono=telefono
        self.nivel_educativo=nivel_educativo
        self.ocupacion=ocupacion
        self.departamento=departamento
        self.municipio=municipio
        self.barrio=barrio
        self.estrato=estrato
        self.tipo_vivienda=tipo_vivienda        
        self.servicios_publicos=servicios_publicos
        self.numero_personas=numero_personas
        self.ingresos_hogar=ingresos_hogar
        self.gastos_hogar=gastos_hogar
        self.clasificacion=clasificacion

db.create_all()

class CiudadanoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','numero_documento','fecha_nacimiento','sexo','telefono','nivel_educativo','ocupacion','departamento', 'municipio','barrio','estrato','tipo_vivienda','servicios_publicos','numero_personas','ingresos_hogar','gastos_hogar','clasificacion')

ciudadano_schema=CiudadanoSchema()
ciudadanos_schema=CiudadanoSchema(many=True)


@app.route('/ciudadanos',methods=['POST'])
def create_ciudadano():
    nombre=request.json['nombre']
    numero_documento=request.json['numero_documento']
    fecha_nacimiento=request.json['fecha_nacimiento']
    sexo=request.json['sexo']
    telefono=request.json['telefono']  
    nivel_educativo=request.json['nivel_educativo'] 
    ocupacion=request.json['ocupacion'] 
    departamento=request.json['departamento']
    municipio=request.json['municipio']
    barrio=request.json['barrio']
    estrato=request.json['estrato']
    tipo_vivienda=request.json['tipo_vivienda']  
    servicios_publicos=request.json['servicios_publicos'] 
    numero_personas=request.json['numero_personas']   
    ingresos_hogar=request.json['ingresos_hogar'] 
    gastos_hogar=request.json['gastos_hogar'] 
    clasificacion=request.json['clasificacion']

    new_ciudadano = Ciudadano(nombre,numero_documento,fecha_nacimiento,sexo,telefono,nivel_educativo,ocupacion,departamento,municipio,barrio,estrato,tipo_vivienda,servicios_publicos,numero_personas,ingresos_hogar,gastos_hogar,clasificacion)

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

    nombre=request.json['nombre']
    numero_documento=request.json['numero_documento']
    fecha_nacimiento=request.json['fecha_nacimiento']
    sexo=request.json['sexo']
    telefono=request.json['telefono']  
    nivel_educativo=request.json['nivel_educativo'] 
    ocupacion=request.json['ocupacion'] 
    departamento=request.json['departamento']
    municipio=request.json['municipio']
    barrio=request.json['barrio']
    estrato=request.json['estrato']
    tipo_vivienda=request.json['tipo_vivienda']  
    servicios_publicos=request.json['servicios_publicos'] 
    numero_personas=request.json['numero_personas']   
    ingresos_hogar=request.json['ingresos_hogar'] 
    gastos_hogar=request.json['gastos_hogar'] 
    clasificacion=request.json['clasificacion']

    ciudadano.nombre=nombre
    ciudadano.numero_documento=numero_documento
    ciudadano.fecha_nacimiento=fecha_nacimiento
    ciudadano.sexo=sexo
    ciudadano.telefono=telefono
    ciudadano.nivel_educativo=nivel_educativo
    ciudadano.ocupacion=ocupacion
    ciudadano.departamento=departamento
    ciudadano.municipio=municipio
    ciudadano.barrio=barrio
    ciudadano.estrato=estrato
    ciudadano.tipo_vivienda=tipo_vivienda
    ciudadano.servicios_publicos=servicios_publicos
    ciudadano.numero_personas=numero_personas
    ciudadano.ingresos_hogar=ingresos_hogar
    ciudadano.gastos_hogar=gastos_hogar
    ciudadano.clasificacion=clasificacion

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