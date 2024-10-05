# Generated from ../grammars/IDL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IDLParser import IDLParser
else:
    from IDLParser import IDLParser

# This class defines a complete generic visitor for a parse tree produced by IDLParser.

class IDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IDLParser#specification.
    def visitSpecification(self, ctx:IDLParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#definition.
    def visitDefinition(self, ctx:IDLParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#module.
    def visitModule(self, ctx:IDLParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_or_forward_decl.
    def visitInterface_or_forward_decl(self, ctx:IDLParser.Interface_or_forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_decl.
    def visitInterface_decl(self, ctx:IDLParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#forward_decl.
    def visitForward_decl(self, ctx:IDLParser.Forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_header.
    def visitInterface_header(self, ctx:IDLParser.Interface_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_body.
    def visitInterface_body(self, ctx:IDLParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#export_.
    def visitExport_(self, ctx:IDLParser.Export_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_inheritance_spec.
    def visitInterface_inheritance_spec(self, ctx:IDLParser.Interface_inheritance_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_name.
    def visitInterface_name(self, ctx:IDLParser.Interface_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#a_scoped_name.
    def visitA_scoped_name(self, ctx:IDLParser.A_scoped_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#scoped_name.
    def visitScoped_name(self, ctx:IDLParser.Scoped_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value.
    def visitValue(self, ctx:IDLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_forward_decl.
    def visitValue_forward_decl(self, ctx:IDLParser.Value_forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_box_decl.
    def visitValue_box_decl(self, ctx:IDLParser.Value_box_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_abs_decl.
    def visitValue_abs_decl(self, ctx:IDLParser.Value_abs_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_decl.
    def visitValue_decl(self, ctx:IDLParser.Value_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_header.
    def visitValue_header(self, ctx:IDLParser.Value_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_inheritance_spec.
    def visitValue_inheritance_spec(self, ctx:IDLParser.Value_inheritance_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_name.
    def visitValue_name(self, ctx:IDLParser.Value_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_element.
    def visitValue_element(self, ctx:IDLParser.Value_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#state_member.
    def visitState_member(self, ctx:IDLParser.State_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#init_decl.
    def visitInit_decl(self, ctx:IDLParser.Init_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#init_param_decls.
    def visitInit_param_decls(self, ctx:IDLParser.Init_param_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#init_param_decl.
    def visitInit_param_decl(self, ctx:IDLParser.Init_param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#init_param_attribute.
    def visitInit_param_attribute(self, ctx:IDLParser.Init_param_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#const_decl.
    def visitConst_decl(self, ctx:IDLParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#const_type.
    def visitConst_type(self, ctx:IDLParser.Const_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#const_exp.
    def visitConst_exp(self, ctx:IDLParser.Const_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#or_expr.
    def visitOr_expr(self, ctx:IDLParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#xor_expr.
    def visitXor_expr(self, ctx:IDLParser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#and_expr.
    def visitAnd_expr(self, ctx:IDLParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#shift_expr.
    def visitShift_expr(self, ctx:IDLParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#add_expr.
    def visitAdd_expr(self, ctx:IDLParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#mult_expr.
    def visitMult_expr(self, ctx:IDLParser.Mult_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unary_expr.
    def visitUnary_expr(self, ctx:IDLParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unary_operator.
    def visitUnary_operator(self, ctx:IDLParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#primary_expr.
    def visitPrimary_expr(self, ctx:IDLParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#literal.
    def visitLiteral(self, ctx:IDLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#positive_int_const.
    def visitPositive_int_const(self, ctx:IDLParser.Positive_int_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_decl.
    def visitType_decl(self, ctx:IDLParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_declarator.
    def visitType_declarator(self, ctx:IDLParser.Type_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_spec.
    def visitType_spec(self, ctx:IDLParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#simple_type_spec.
    def visitSimple_type_spec(self, ctx:IDLParser.Simple_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bitfield_type_spec.
    def visitBitfield_type_spec(self, ctx:IDLParser.Bitfield_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#base_type_spec.
    def visitBase_type_spec(self, ctx:IDLParser.Base_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#template_type_spec.
    def visitTemplate_type_spec(self, ctx:IDLParser.Template_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#constr_type_spec.
    def visitConstr_type_spec(self, ctx:IDLParser.Constr_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#simple_declarators.
    def visitSimple_declarators(self, ctx:IDLParser.Simple_declaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#declarators.
    def visitDeclarators(self, ctx:IDLParser.DeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#declarator.
    def visitDeclarator(self, ctx:IDLParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#simple_declarator.
    def visitSimple_declarator(self, ctx:IDLParser.Simple_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#complex_declarator.
    def visitComplex_declarator(self, ctx:IDLParser.Complex_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#floating_pt_type.
    def visitFloating_pt_type(self, ctx:IDLParser.Floating_pt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#integer_type.
    def visitInteger_type(self, ctx:IDLParser.Integer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#signed_int.
    def visitSigned_int(self, ctx:IDLParser.Signed_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#signed_tiny_int.
    def visitSigned_tiny_int(self, ctx:IDLParser.Signed_tiny_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#signed_short_int.
    def visitSigned_short_int(self, ctx:IDLParser.Signed_short_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#signed_long_int.
    def visitSigned_long_int(self, ctx:IDLParser.Signed_long_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#signed_longlong_int.
    def visitSigned_longlong_int(self, ctx:IDLParser.Signed_longlong_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unsigned_int.
    def visitUnsigned_int(self, ctx:IDLParser.Unsigned_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unsigned_tiny_int.
    def visitUnsigned_tiny_int(self, ctx:IDLParser.Unsigned_tiny_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unsigned_short_int.
    def visitUnsigned_short_int(self, ctx:IDLParser.Unsigned_short_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unsigned_long_int.
    def visitUnsigned_long_int(self, ctx:IDLParser.Unsigned_long_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#unsigned_longlong_int.
    def visitUnsigned_longlong_int(self, ctx:IDLParser.Unsigned_longlong_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#char_type.
    def visitChar_type(self, ctx:IDLParser.Char_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#wide_char_type.
    def visitWide_char_type(self, ctx:IDLParser.Wide_char_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#boolean_type.
    def visitBoolean_type(self, ctx:IDLParser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#octet_type.
    def visitOctet_type(self, ctx:IDLParser.Octet_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#any_type.
    def visitAny_type(self, ctx:IDLParser.Any_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#object_type.
    def visitObject_type(self, ctx:IDLParser.Object_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_decl.
    def visitAnnotation_decl(self, ctx:IDLParser.Annotation_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_def.
    def visitAnnotation_def(self, ctx:IDLParser.Annotation_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_header.
    def visitAnnotation_header(self, ctx:IDLParser.Annotation_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_inheritance_spec.
    def visitAnnotation_inheritance_spec(self, ctx:IDLParser.Annotation_inheritance_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_body.
    def visitAnnotation_body(self, ctx:IDLParser.Annotation_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_member.
    def visitAnnotation_member(self, ctx:IDLParser.Annotation_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_forward_dcl.
    def visitAnnotation_forward_dcl(self, ctx:IDLParser.Annotation_forward_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bitset_type.
    def visitBitset_type(self, ctx:IDLParser.Bitset_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bitfield.
    def visitBitfield(self, ctx:IDLParser.BitfieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bitfield_spec.
    def visitBitfield_spec(self, ctx:IDLParser.Bitfield_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bitmask_type.
    def visitBitmask_type(self, ctx:IDLParser.Bitmask_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#bit_values.
    def visitBit_values(self, ctx:IDLParser.Bit_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#struct_type.
    def visitStruct_type(self, ctx:IDLParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#member_list.
    def visitMember_list(self, ctx:IDLParser.Member_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#member.
    def visitMember(self, ctx:IDLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#union_type.
    def visitUnion_type(self, ctx:IDLParser.Union_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#switch_type_spec.
    def visitSwitch_type_spec(self, ctx:IDLParser.Switch_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#switch_body.
    def visitSwitch_body(self, ctx:IDLParser.Switch_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#case_stmt.
    def visitCase_stmt(self, ctx:IDLParser.Case_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#case_label.
    def visitCase_label(self, ctx:IDLParser.Case_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#element_spec.
    def visitElement_spec(self, ctx:IDLParser.Element_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#enum_type.
    def visitEnum_type(self, ctx:IDLParser.Enum_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#enumerator.
    def visitEnumerator(self, ctx:IDLParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#sequence_type.
    def visitSequence_type(self, ctx:IDLParser.Sequence_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#set_type.
    def visitSet_type(self, ctx:IDLParser.Set_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#map_type.
    def visitMap_type(self, ctx:IDLParser.Map_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#string_type.
    def visitString_type(self, ctx:IDLParser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#wide_string_type.
    def visitWide_string_type(self, ctx:IDLParser.Wide_string_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#array_declarator.
    def visitArray_declarator(self, ctx:IDLParser.Array_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#fixed_array_size.
    def visitFixed_array_size(self, ctx:IDLParser.Fixed_array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#attr_decl.
    def visitAttr_decl(self, ctx:IDLParser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#except_decl.
    def visitExcept_decl(self, ctx:IDLParser.Except_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#op_decl.
    def visitOp_decl(self, ctx:IDLParser.Op_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#op_attribute.
    def visitOp_attribute(self, ctx:IDLParser.Op_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#op_type_spec.
    def visitOp_type_spec(self, ctx:IDLParser.Op_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#parameter_decls.
    def visitParameter_decls(self, ctx:IDLParser.Parameter_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#param_decl.
    def visitParam_decl(self, ctx:IDLParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#param_attribute.
    def visitParam_attribute(self, ctx:IDLParser.Param_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#raises_expr.
    def visitRaises_expr(self, ctx:IDLParser.Raises_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#context_expr.
    def visitContext_expr(self, ctx:IDLParser.Context_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#param_type_spec.
    def visitParam_type_spec(self, ctx:IDLParser.Param_type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#fixed_pt_type.
    def visitFixed_pt_type(self, ctx:IDLParser.Fixed_pt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#fixed_pt_const_type.
    def visitFixed_pt_const_type(self, ctx:IDLParser.Fixed_pt_const_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#value_base_type.
    def visitValue_base_type(self, ctx:IDLParser.Value_base_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#constr_forward_decl.
    def visitConstr_forward_decl(self, ctx:IDLParser.Constr_forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#import_decl.
    def visitImport_decl(self, ctx:IDLParser.Import_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#imported_scope.
    def visitImported_scope(self, ctx:IDLParser.Imported_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_id_decl.
    def visitType_id_decl(self, ctx:IDLParser.Type_id_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#type_prefix_decl.
    def visitType_prefix_decl(self, ctx:IDLParser.Type_prefix_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#readonly_attr_spec.
    def visitReadonly_attr_spec(self, ctx:IDLParser.Readonly_attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#readonly_attr_declarator.
    def visitReadonly_attr_declarator(self, ctx:IDLParser.Readonly_attr_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#attr_spec.
    def visitAttr_spec(self, ctx:IDLParser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#attr_declarator.
    def visitAttr_declarator(self, ctx:IDLParser.Attr_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#attr_raises_expr.
    def visitAttr_raises_expr(self, ctx:IDLParser.Attr_raises_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#get_excep_expr.
    def visitGet_excep_expr(self, ctx:IDLParser.Get_excep_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#set_excep_expr.
    def visitSet_excep_expr(self, ctx:IDLParser.Set_excep_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#exception_list.
    def visitException_list(self, ctx:IDLParser.Exception_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component.
    def visitComponent(self, ctx:IDLParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_forward_decl.
    def visitComponent_forward_decl(self, ctx:IDLParser.Component_forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_decl.
    def visitComponent_decl(self, ctx:IDLParser.Component_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_header.
    def visitComponent_header(self, ctx:IDLParser.Component_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#supported_interface_spec.
    def visitSupported_interface_spec(self, ctx:IDLParser.Supported_interface_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_inheritance_spec.
    def visitComponent_inheritance_spec(self, ctx:IDLParser.Component_inheritance_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_body.
    def visitComponent_body(self, ctx:IDLParser.Component_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#component_export.
    def visitComponent_export(self, ctx:IDLParser.Component_exportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#provides_decl.
    def visitProvides_decl(self, ctx:IDLParser.Provides_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#interface_type.
    def visitInterface_type(self, ctx:IDLParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#uses_decl.
    def visitUses_decl(self, ctx:IDLParser.Uses_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#emits_decl.
    def visitEmits_decl(self, ctx:IDLParser.Emits_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#publishes_decl.
    def visitPublishes_decl(self, ctx:IDLParser.Publishes_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#consumes_decl.
    def visitConsumes_decl(self, ctx:IDLParser.Consumes_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#home_decl.
    def visitHome_decl(self, ctx:IDLParser.Home_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#home_header.
    def visitHome_header(self, ctx:IDLParser.Home_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#home_inheritance_spec.
    def visitHome_inheritance_spec(self, ctx:IDLParser.Home_inheritance_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#primary_key_spec.
    def visitPrimary_key_spec(self, ctx:IDLParser.Primary_key_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#home_body.
    def visitHome_body(self, ctx:IDLParser.Home_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#home_export.
    def visitHome_export(self, ctx:IDLParser.Home_exportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#factory_decl.
    def visitFactory_decl(self, ctx:IDLParser.Factory_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#finder_decl.
    def visitFinder_decl(self, ctx:IDLParser.Finder_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#event.
    def visitEvent(self, ctx:IDLParser.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#event_forward_decl.
    def visitEvent_forward_decl(self, ctx:IDLParser.Event_forward_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#event_abs_decl.
    def visitEvent_abs_decl(self, ctx:IDLParser.Event_abs_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#event_decl.
    def visitEvent_decl(self, ctx:IDLParser.Event_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#event_header.
    def visitEvent_header(self, ctx:IDLParser.Event_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annapps.
    def visitAnnapps(self, ctx:IDLParser.AnnappsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_appl.
    def visitAnnotation_appl(self, ctx:IDLParser.Annotation_applContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_appl_params.
    def visitAnnotation_appl_params(self, ctx:IDLParser.Annotation_appl_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#annotation_appl_param.
    def visitAnnotation_appl_param(self, ctx:IDLParser.Annotation_appl_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IDLParser#identifier.
    def visitIdentifier(self, ctx:IDLParser.IdentifierContext):
        return self.visitChildren(ctx)



del IDLParser