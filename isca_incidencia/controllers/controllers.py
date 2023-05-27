from odoo import http
from odoo.http import json, request
from datetime import datetime

class CategoryController(http.Controller):
    @http.route(['/iscaIncidencia/getCategory',"/iscaIncidencia/getCategory/<int:categoryid>"], auth='public', type='http')
    def getCategory(self, categoryid=None, **kw):
        if categoryid:
            domain=[("id","=", categoryid)]
        else:
            domain=[]
        category_data = http.request.env["isca_incidencia.category_model"].sudo().search_read(domain,["name","descripcion","photo"])
        
        data = {"status":200, "data":[]}
        for category in category_data:
            if 'photo' in category:
                category['photo'] = category['photo'].decode('utf-8')
            data["data"].append(category)

        return http.Response(json.dumps(data), mimetype='application/json')
##################################################### Usuario ############################################################################
class UsuarioController(http.Controller):
    @http.route(['/iscaIncidencia/getUsuario', "/iscaIncidencia/getUsuario/<int:usuarioid>"], auth='public', type='http')
    def getUsuario(self, usuarioid=None, **kw):
        if usuarioid:
            domain=[("id","=", usuarioid)]
        else:
            domain=[]
        usuariodata=http.request.env["isca_incidencia.usuario_model"].sudo().search_read(domain,["name","apellidos","usuario","password","reparador","registro","incidenciasCreadas","incidenciasAsignadas","rol","inventarioCreado","categorias","activo"])
        data={"status":200,
              "data":usuariodata}    
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/iscaIncidencia/addUsuario', auth='public', type='json', method="POST")
    def addUsuario(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["isca_incidencia.usuario_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateUsuario/<int:usuarioid>', auth='public', type='json', method="PUT")
    def updateUsuario(self, usuarioid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.usuario_model"].sudo().search([("id", "=", usuarioid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteUsuario/', auth='public', type='json', method="DELETE")
    def deleteUsuario(self, **kw):
        usuarioid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.usuario_model"].sudo().search([("id", "=", usuarioid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data



 ###################################################    CATEGORIA       #####################################################################
class CategoriaController(http.Controller):
    @http.route(['/iscaIncidencia/getCategoria', "/iscaIncidencia/getCategoria/<int:categoriaid>"], auth='public', type='http')
    def getCategoria(self, categoriaid=None, **kw):
        if categoriaid:
            domain=[("id","=", categoriaid)]
        else:
            domain=[]
        categoriadata=http.request.env["isca_incidencia.categoria_model"].sudo().search_read(domain,["name","descripcion","usuarios","inventario","responsable"])
        data={"status":200,
              "data":categoriadata}    
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/iscaIncidencia/addCategoria', auth='public', type='json', method="POST")
    def addCategoria(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["isca_incidencia.categoria_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateCategoria/<int:categoriaid>', auth='public', type='json', method="PUT")
    def updateProduct(self, categoriaid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.categoria_model"].sudo().search([("id", "=", categoriaid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteCategoria/', auth='public', type='json', method="DELETE")
    def deleteCat(self, **kw):
        categoriaid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.categoria_model"].sudo().search([("id", "=", categoriaid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
################################################            ROL         ###############################################################
class RolController(http.Controller):
    @http.route(['/iscaIncidencia/getRol', "/iscaIncidencia/getRol/<int:rolid>"], auth='public', type='http')
    def getRol(self, rolid=None, **kw):
        if rolid:
            domain=[("id","=", rolid)]
        else:
            domain=[]
        roldata=http.request.env["isca_incidencia.rol_model"].sudo().search_read(domain,["name","descripcion","reparador","usuarios"])
        data={"status":200,
              "data":roldata}    
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/iscaIncidencia/addRol', auth='public', type='json', method="POST")
    def addRol(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.rol_model"].sudo().create(response)
            data = { "status": 200,
                    "id": result.id }
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e }
            return data

    @http.route('/iscaIncidencia/updateRol/<int:rolid>', auth='public', type='json', method="PUT")
    def updateRol(self, rolid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.rol_model"].sudo().search([("id", "=", rolid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id }
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e }
            return data


    @http.route('/iscaIncidencia/deleteRol/', auth='public', type='json', method="DELETE")
    def deleteRol(self, **kw):
        rolid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.rol_model"].sudo().search([("id", "=", rolid)])
            result.unlink()
            data = { "status": 200 }
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e }
            return data

#############################################Ubicacion#######################################33


class UbicacionController(http.Controller):
    @http.route(['/iscaIncidencia/getUbicacion', "/iscaIncidencia/getUbicacion/<int:ubicacionid>"], auth='public', type='http')
    def getUbicacion(self, ubicacionid=None, **kw):
        if ubicacionid:
            domain=[("id","=", ubicacionid)]
        else:
            domain=[]
        ubicaciondata=http.request.env["isca_incidencia.ubicacion_model"].sudo().search_read(domain,["name","descripcion","inventario","incidencia"])
        data={"status":200,
              "data":ubicaciondata}    
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")



    @http.route('/iscaIncidencia/addUbicacion', auth='public', type='json', method="POST")
    def addUbicacion(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["isca_incidencia.ubicacion_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateUbicacion/<int:ubicacionid>', auth='public', type='json', method="PUT")
    def updateUbicacion(self, ubicacionid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.ubicacion_model"].sudo().search([("id", "=", ubicacionid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteUbicacion/', auth='public', type='json', method="DELETE")
    def deleteUbicacion(self, **kw):
        ubicacionid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.ubicacion_model"].sudo().search([("id", "=", ubicacionid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
########################################################        INVENTARIO          ##############################################################################################333
class InventarioController(http.Controller):
    @http.route(['/iscaIncidencia/getInventario', '/iscaIncidencia/getInventario/<int:inventarioid>'], auth='public', type='http')
    def getInventario(self, inventarioid=None, **kw):
        if inventarioid:
            domain = [("id", "=", inventarioid)]
        else:
            domain = []
        inventario_data = http.request.env["isca_incidencia.inventario_model"].sudo().search_read(domain, ["name", "descripcion", "cantidad", "fechaCreacion", "icono", "etiqueta", "etiquetable", "conIncidencia", "categoria", "usuario", "ubicacion", "masImagenes","incidencias","facturas","activo"])

        data = {"status": 200, "data": []}
        for inventario in inventario_data:
            if inventario['icono']:
                inventario['icono'] = inventario['icono'].decode('utf-8')
            inventario['fechaCreacion'] = datetime.strftime(inventario['fechaCreacion'], "%Y-%m-%d %H:%M:%S")
            data["data"].append(inventario)

        return http.Response(json.dumps(data), mimetype='application/json')
    
    
    @http.route('/iscaIncidencia/addInventario', auth='public', type='json', method="POST")
    def addInventario(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.inventario_model"].sudo().create(response)
            data = {"status": 200,
                "id": result.id
            }
            return data
        except Exception as e:
            data = { "status": 404,
                "error": e}
            return data

    @http.route('/iscaIncidencia/updateInventario/<int:inventarioid>', auth='public', type='json', method="PUT")
    def updateInventario(self, inventarioid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.inventario_model"].sudo().search([("id", "=", inventarioid)])
            result.write(response)
            data = { "status": 200, "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404, "error": e}
            return data

    @http.route('/iscaIncidencia/deleteInventario/', auth='public', type='json', method="DELETE")
    def deleteInventario(self, **kw):
        inventarioid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.inventario_model"].sudo().search([("id", "=", inventarioid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404, "error": e}
            return data
    ########################################################INCIDENCIA###############################################
class IncidenciaController(http.Controller):
    @http.route(['/iscaIncidencia/getIncidencia', '/iscaIncidencia/getIncidencia/<int:incidenciaid>'], auth='public', type='http')
    def getIncidencia(self, incidenciaid=None, **kw):
        if incidenciaid:
            domain = [("id", "=", incidenciaid)]
        else:
            domain = []
        incidencia_data = http.request.env["isca_incidencia.incidencia_model"].sudo().search_read(domain, ["name", "descripcion", "fechaAbertura", "fechaCierre", "foto", "estado", "inventario", "registro", "creador", "asignado", "ubicacion", "masImagenes"])

        data = {"status": 200, "data": []}
        for incidencia in incidencia_data:
            if incidencia['foto']:
                incidencia['foto'] = incidencia['foto'].decode('utf-8')
            incidencia['fechaAbertura'] = datetime.strftime(incidencia['fechaAbertura'], "%Y-%m-%d %H:%M:%S")
            if incidencia['fechaCierre']:
                incidencia['fechaCierre'] = datetime.strftime(incidencia['fechaCierre'], "%Y-%m-%d %H:%M:%S")
            data["data"].append(incidencia)

        return http.Response(json.dumps(data), mimetype='application/json')

    @http.route('/iscaIncidencia/addIncidencia', auth='public', type='json', method="POST")
    def addIncidencia(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.incidencia_model"].sudo().create(response)
            data = { "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data = { "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateIncidencia/<int:incidenciaid>', auth='public', type='json', method="PUT")
    def updateIncidencia(self, incidenciaid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.incidencia_model"].sudo().search([("id", "=", incidenciaid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteIncidencia/', auth='public', type='json', method="DELETE")
    def deleteIncidencia(self, **kw):
        incidenciaid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.incidencia_model"].sudo().search([("id", "=", incidenciaid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
    

########################################################REGISTRO###############################################
class RegistroController(http.Controller):
    @http.route(['/iscaIncidencia/getRegistro', '/iscaIncidencia/getRegistro/<int:registroid>'], auth='public', type='http')
    def getRegistro(self, registroid=None, **kw):
        if registroid:
            domain = [("id", "=", registroid)]
        else:
            domain = []
        registro_data = http.request.env["isca_incidencia.registro_model"].sudo().search_read(domain, ["name", "comentario", "usuario", "incidencia"])

        data = {"status": 200, "data": []}
        for registro in registro_data:
            registro['name'] = datetime.strftime(registro['name'], "%Y-%m-%d %H:%M:%S")
            data["data"].append(registro)

        return http.Response(json.dumps(data), mimetype='application/json')
    
    @http.route('/iscaIncidencia/addRegistro', auth='public', type='json', method="POST")
    def addRegistro(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["isca_incidencia.registro_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateRegistro/<int:registroid>', auth='public', type='json', method="PUT")
    def updateRegistro(self, registroid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.registro_model"].sudo().search([("id", "=", registroid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteRegistro/', auth='public', type='json', method="DELETE")
    def deleteRegistro(self, **kw):
        registroid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.registro_model"].sudo().search([("id", "=", registroid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    

        ########################################################FACTURA###############################################

class FacturaController(http.Controller):
    @http.route(['/iscaIncidencia/getFactura', '/iscaIncidencia/getFactura/<int:facturaid>'], auth='public', type='http')
    def getFactura(self, facturaid=None, **kw):
        if facturaid:
            domain = [("id", "=", facturaid)]
        else:
            domain = []
        factura_data = http.request.env["isca_incidencia.factura_model"].sudo().search_read(domain, ["name", "fechaCreacion", "inventario"])

        data = {"status": 200, "data": []}
        for factura in factura_data:
            if factura['name']:
                factura['name'] = factura['name'].decode('utf-8')
            factura['fechaCreacion'] = datetime.strftime(factura['fechaCreacion'], "%Y-%m-%d %H:%M:%S")
            data["data"].append(factura)
        return http.Response(json.dumps(data), mimetype='application/json')

    @http.route('/iscaIncidencia/addFactura', auth='public', type='json', method="POST")
    def addFactura(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["isca_incidencia.factura_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/iscaIncidencia/updateFactura/<int:facturaid>', auth='public', type='json', method="PUT")
    def updateFactura(self, facturaid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.factura_model"].sudo().search([("id", "=", facturaid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/iscaIncidencia/deleteFactura/', auth='public', type='json', method="DELETE")
    def deleteFactura(self, **kw):
        facturaid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.factura_model"].sudo().search([("id", "=", facturaid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

########################################################Album###############################################
class AlbumController(http.Controller):
    @http.route(['/iscaIncidencia/getAlbum', '/iscaIncidencia/getAlbum/<int:albumid>'], auth='public', type='http')
    def getAlbum(self, albumid=None, **kw):
        if albumid:
            domain = [("id", "=", albumid)]
        else:
            domain = []
        album_data = http.request.env["isca_incidencia.album_model"].sudo().search_read(domain, ["name", "fechaCreacion", "inventario", "incidencia"])

        data = {"status": 200, "data": []}
        for album in album_data:
            if album['name']:
                album['name'] = album['name'].decode('utf-8')
            album['fechaCreacion'] = datetime.strftime(album['fechaCreacion'], "%Y-%m-%d %H:%M:%S")
            data["data"].append(album)

        return http.Response(json.dumps(data), mimetype='application/json')
    
    @http.route('/iscaIncidencia/addAlbum', auth='public', type='json', method="POST")
    def addAlbum(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.album_model"].sudo().create(response)
            data = {"status": 200, "id": result.id}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

    @http.route('/iscaIncidencia/updateAlbum/<int:albumid>', auth='public', type='json', method="PUT")
    def updateAlbum(self, albumid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["isca_incidencia.album_model"].sudo().search([("id", "=", albumid)])
            result.write(response)
            data = {"status": 200, "id": result.id}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data

    @http.route('/iscaIncidencia/deleteAlbum/', auth='public', type='json', method="DELETE")
    def deleteAlbum(self, **kw):
        albumid = request.jsonrequest["id"]
        try:
            result = http.request.env["isca_incidencia.album_model"].sudo().search([("id", "=", albumid)])
            result.unlink()
            data = {"status": 200}
            return data
        except Exception as e:
            data = {"status": 404, "error": e}
            return data