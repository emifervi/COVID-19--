# Generated from Covid.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CovidParser import CovidParser
else:
    from CovidParser import CovidParser

# This class defines a complete listener for a parse tree produced by CovidParser.
class CovidListener(ParseTreeListener):

    # Enter a parse tree produced by CovidParser#start.
    def enterStart(self, ctx:CovidParser.StartContext):
        pass

    # Exit a parse tree produced by CovidParser#start.
    def exitStart(self, ctx:CovidParser.StartContext):
        pass


    # Enter a parse tree produced by CovidParser#var_block.
    def enterVar_block(self, ctx:CovidParser.Var_blockContext):
        pass

    # Exit a parse tree produced by CovidParser#var_block.
    def exitVar_block(self, ctx:CovidParser.Var_blockContext):
        pass


    # Enter a parse tree produced by CovidParser#ids_decl.
    def enterIds_decl(self, ctx:CovidParser.Ids_declContext):
        pass

    # Exit a parse tree produced by CovidParser#ids_decl.
    def exitIds_decl(self, ctx:CovidParser.Ids_declContext):
        pass


    # Enter a parse tree produced by CovidParser#ident_decl.
    def enterIdent_decl(self, ctx:CovidParser.Ident_declContext):
        pass

    # Exit a parse tree produced by CovidParser#ident_decl.
    def exitIdent_decl(self, ctx:CovidParser.Ident_declContext):
        pass


    # Enter a parse tree produced by CovidParser#ids.
    def enterIds(self, ctx:CovidParser.IdsContext):
        pass

    # Exit a parse tree produced by CovidParser#ids.
    def exitIds(self, ctx:CovidParser.IdsContext):
        pass


    # Enter a parse tree produced by CovidParser#ident.
    def enterIdent(self, ctx:CovidParser.IdentContext):
        pass

    # Exit a parse tree produced by CovidParser#ident.
    def exitIdent(self, ctx:CovidParser.IdentContext):
        pass


    # Enter a parse tree produced by CovidParser#ident_ind.
    def enterIdent_ind(self, ctx:CovidParser.Ident_indContext):
        pass

    # Exit a parse tree produced by CovidParser#ident_ind.
    def exitIdent_ind(self, ctx:CovidParser.Ident_indContext):
        pass


    # Enter a parse tree produced by CovidParser#tipo.
    def enterTipo(self, ctx:CovidParser.TipoContext):
        pass

    # Exit a parse tree produced by CovidParser#tipo.
    def exitTipo(self, ctx:CovidParser.TipoContext):
        pass


    # Enter a parse tree produced by CovidParser#tipo_atom.
    def enterTipo_atom(self, ctx:CovidParser.Tipo_atomContext):
        pass

    # Exit a parse tree produced by CovidParser#tipo_atom.
    def exitTipo_atom(self, ctx:CovidParser.Tipo_atomContext):
        pass


    # Enter a parse tree produced by CovidParser#func.
    def enterFunc(self, ctx:CovidParser.FuncContext):
        pass

    # Exit a parse tree produced by CovidParser#func.
    def exitFunc(self, ctx:CovidParser.FuncContext):
        pass


    # Enter a parse tree produced by CovidParser#return_type.
    def enterReturn_type(self, ctx:CovidParser.Return_typeContext):
        pass

    # Exit a parse tree produced by CovidParser#return_type.
    def exitReturn_type(self, ctx:CovidParser.Return_typeContext):
        pass


    # Enter a parse tree produced by CovidParser#params.
    def enterParams(self, ctx:CovidParser.ParamsContext):
        pass

    # Exit a parse tree produced by CovidParser#params.
    def exitParams(self, ctx:CovidParser.ParamsContext):
        pass


    # Enter a parse tree produced by CovidParser#param.
    def enterParam(self, ctx:CovidParser.ParamContext):
        pass

    # Exit a parse tree produced by CovidParser#param.
    def exitParam(self, ctx:CovidParser.ParamContext):
        pass


    # Enter a parse tree produced by CovidParser#block.
    def enterBlock(self, ctx:CovidParser.BlockContext):
        pass

    # Exit a parse tree produced by CovidParser#block.
    def exitBlock(self, ctx:CovidParser.BlockContext):
        pass


    # Enter a parse tree produced by CovidParser#main.
    def enterMain(self, ctx:CovidParser.MainContext):
        pass

    # Exit a parse tree produced by CovidParser#main.
    def exitMain(self, ctx:CovidParser.MainContext):
        pass


    # Enter a parse tree produced by CovidParser#statement.
    def enterStatement(self, ctx:CovidParser.StatementContext):
        pass

    # Exit a parse tree produced by CovidParser#statement.
    def exitStatement(self, ctx:CovidParser.StatementContext):
        pass


    # Enter a parse tree produced by CovidParser#assignment.
    def enterAssignment(self, ctx:CovidParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CovidParser#assignment.
    def exitAssignment(self, ctx:CovidParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CovidParser#call.
    def enterCall(self, ctx:CovidParser.CallContext):
        pass

    # Exit a parse tree produced by CovidParser#call.
    def exitCall(self, ctx:CovidParser.CallContext):
        pass


    # Enter a parse tree produced by CovidParser#args.
    def enterArgs(self, ctx:CovidParser.ArgsContext):
        pass

    # Exit a parse tree produced by CovidParser#args.
    def exitArgs(self, ctx:CovidParser.ArgsContext):
        pass


    # Enter a parse tree produced by CovidParser#regresa.
    def enterRegresa(self, ctx:CovidParser.RegresaContext):
        pass

    # Exit a parse tree produced by CovidParser#regresa.
    def exitRegresa(self, ctx:CovidParser.RegresaContext):
        pass


    # Enter a parse tree produced by CovidParser#read.
    def enterRead(self, ctx:CovidParser.ReadContext):
        pass

    # Exit a parse tree produced by CovidParser#read.
    def exitRead(self, ctx:CovidParser.ReadContext):
        pass


    # Enter a parse tree produced by CovidParser#write.
    def enterWrite(self, ctx:CovidParser.WriteContext):
        pass

    # Exit a parse tree produced by CovidParser#write.
    def exitWrite(self, ctx:CovidParser.WriteContext):
        pass


    # Enter a parse tree produced by CovidParser#impr.
    def enterImpr(self, ctx:CovidParser.ImprContext):
        pass

    # Exit a parse tree produced by CovidParser#impr.
    def exitImpr(self, ctx:CovidParser.ImprContext):
        pass


    # Enter a parse tree produced by CovidParser#imprs.
    def enterImprs(self, ctx:CovidParser.ImprsContext):
        pass

    # Exit a parse tree produced by CovidParser#imprs.
    def exitImprs(self, ctx:CovidParser.ImprsContext):
        pass


    # Enter a parse tree produced by CovidParser#decision.
    def enterDecision(self, ctx:CovidParser.DecisionContext):
        pass

    # Exit a parse tree produced by CovidParser#decision.
    def exitDecision(self, ctx:CovidParser.DecisionContext):
        pass


    # Enter a parse tree produced by CovidParser#else_block.
    def enterElse_block(self, ctx:CovidParser.Else_blockContext):
        pass

    # Exit a parse tree produced by CovidParser#else_block.
    def exitElse_block(self, ctx:CovidParser.Else_blockContext):
        pass


    # Enter a parse tree produced by CovidParser#while_loop.
    def enterWhile_loop(self, ctx:CovidParser.While_loopContext):
        pass

    # Exit a parse tree produced by CovidParser#while_loop.
    def exitWhile_loop(self, ctx:CovidParser.While_loopContext):
        pass


    # Enter a parse tree produced by CovidParser#for_loop.
    def enterFor_loop(self, ctx:CovidParser.For_loopContext):
        pass

    # Exit a parse tree produced by CovidParser#for_loop.
    def exitFor_loop(self, ctx:CovidParser.For_loopContext):
        pass


    # Enter a parse tree produced by CovidParser#for_asgn.
    def enterFor_asgn(self, ctx:CovidParser.For_asgnContext):
        pass

    # Exit a parse tree produced by CovidParser#for_asgn.
    def exitFor_asgn(self, ctx:CovidParser.For_asgnContext):
        pass


    # Enter a parse tree produced by CovidParser#expr.
    def enterExpr(self, ctx:CovidParser.ExprContext):
        pass

    # Exit a parse tree produced by CovidParser#expr.
    def exitExpr(self, ctx:CovidParser.ExprContext):
        pass


    # Enter a parse tree produced by CovidParser#exprs.
    def enterExprs(self, ctx:CovidParser.ExprsContext):
        pass

    # Exit a parse tree produced by CovidParser#exprs.
    def exitExprs(self, ctx:CovidParser.ExprsContext):
        pass


    # Enter a parse tree produced by CovidParser#and_term.
    def enterAnd_term(self, ctx:CovidParser.And_termContext):
        pass

    # Exit a parse tree produced by CovidParser#and_term.
    def exitAnd_term(self, ctx:CovidParser.And_termContext):
        pass


    # Enter a parse tree produced by CovidParser#and_terms.
    def enterAnd_terms(self, ctx:CovidParser.And_termsContext):
        pass

    # Exit a parse tree produced by CovidParser#and_terms.
    def exitAnd_terms(self, ctx:CovidParser.And_termsContext):
        pass


    # Enter a parse tree produced by CovidParser#comp_term.
    def enterComp_term(self, ctx:CovidParser.Comp_termContext):
        pass

    # Exit a parse tree produced by CovidParser#comp_term.
    def exitComp_term(self, ctx:CovidParser.Comp_termContext):
        pass


    # Enter a parse tree produced by CovidParser#comp_op.
    def enterComp_op(self, ctx:CovidParser.Comp_opContext):
        pass

    # Exit a parse tree produced by CovidParser#comp_op.
    def exitComp_op(self, ctx:CovidParser.Comp_opContext):
        pass


    # Enter a parse tree produced by CovidParser#rel_term.
    def enterRel_term(self, ctx:CovidParser.Rel_termContext):
        pass

    # Exit a parse tree produced by CovidParser#rel_term.
    def exitRel_term(self, ctx:CovidParser.Rel_termContext):
        pass


    # Enter a parse tree produced by CovidParser#rel_op.
    def enterRel_op(self, ctx:CovidParser.Rel_opContext):
        pass

    # Exit a parse tree produced by CovidParser#rel_op.
    def exitRel_op(self, ctx:CovidParser.Rel_opContext):
        pass


    # Enter a parse tree produced by CovidParser#artm_term.
    def enterArtm_term(self, ctx:CovidParser.Artm_termContext):
        pass

    # Exit a parse tree produced by CovidParser#artm_term.
    def exitArtm_term(self, ctx:CovidParser.Artm_termContext):
        pass


    # Enter a parse tree produced by CovidParser#artm_terms.
    def enterArtm_terms(self, ctx:CovidParser.Artm_termsContext):
        pass

    # Exit a parse tree produced by CovidParser#artm_terms.
    def exitArtm_terms(self, ctx:CovidParser.Artm_termsContext):
        pass


    # Enter a parse tree produced by CovidParser#fact_term.
    def enterFact_term(self, ctx:CovidParser.Fact_termContext):
        pass

    # Exit a parse tree produced by CovidParser#fact_term.
    def exitFact_term(self, ctx:CovidParser.Fact_termContext):
        pass


    # Enter a parse tree produced by CovidParser#fact_terms.
    def enterFact_terms(self, ctx:CovidParser.Fact_termsContext):
        pass

    # Exit a parse tree produced by CovidParser#fact_terms.
    def exitFact_terms(self, ctx:CovidParser.Fact_termsContext):
        pass


    # Enter a parse tree produced by CovidParser#operand.
    def enterOperand(self, ctx:CovidParser.OperandContext):
        pass

    # Exit a parse tree produced by CovidParser#operand.
    def exitOperand(self, ctx:CovidParser.OperandContext):
        pass


    # Enter a parse tree produced by CovidParser#cte.
    def enterCte(self, ctx:CovidParser.CteContext):
        pass

    # Exit a parse tree produced by CovidParser#cte.
    def exitCte(self, ctx:CovidParser.CteContext):
        pass


    # Enter a parse tree produced by CovidParser#covid.
    def enterCovid(self, ctx:CovidParser.CovidContext):
        pass

    # Exit a parse tree produced by CovidParser#covid.
    def exitCovid(self, ctx:CovidParser.CovidContext):
        pass


    # Enter a parse tree produced by CovidParser#load_file.
    def enterLoad_file(self, ctx:CovidParser.Load_fileContext):
        pass

    # Exit a parse tree produced by CovidParser#load_file.
    def exitLoad_file(self, ctx:CovidParser.Load_fileContext):
        pass


    # Enter a parse tree produced by CovidParser#load_data.
    def enterLoad_data(self, ctx:CovidParser.Load_dataContext):
        pass

    # Exit a parse tree produced by CovidParser#load_data.
    def exitLoad_data(self, ctx:CovidParser.Load_dataContext):
        pass


    # Enter a parse tree produced by CovidParser#avg.
    def enterAvg(self, ctx:CovidParser.AvgContext):
        pass

    # Exit a parse tree produced by CovidParser#avg.
    def exitAvg(self, ctx:CovidParser.AvgContext):
        pass


    # Enter a parse tree produced by CovidParser#moda.
    def enterModa(self, ctx:CovidParser.ModaContext):
        pass

    # Exit a parse tree produced by CovidParser#moda.
    def exitModa(self, ctx:CovidParser.ModaContext):
        pass


    # Enter a parse tree produced by CovidParser#rango.
    def enterRango(self, ctx:CovidParser.RangoContext):
        pass

    # Exit a parse tree produced by CovidParser#rango.
    def exitRango(self, ctx:CovidParser.RangoContext):
        pass


    # Enter a parse tree produced by CovidParser#variance.
    def enterVariance(self, ctx:CovidParser.VarianceContext):
        pass

    # Exit a parse tree produced by CovidParser#variance.
    def exitVariance(self, ctx:CovidParser.VarianceContext):
        pass


    # Enter a parse tree produced by CovidParser#std_dev.
    def enterStd_dev(self, ctx:CovidParser.Std_devContext):
        pass

    # Exit a parse tree produced by CovidParser#std_dev.
    def exitStd_dev(self, ctx:CovidParser.Std_devContext):
        pass


    # Enter a parse tree produced by CovidParser#maxi.
    def enterMaxi(self, ctx:CovidParser.MaxiContext):
        pass

    # Exit a parse tree produced by CovidParser#maxi.
    def exitMaxi(self, ctx:CovidParser.MaxiContext):
        pass


    # Enter a parse tree produced by CovidParser#mini.
    def enterMini(self, ctx:CovidParser.MiniContext):
        pass

    # Exit a parse tree produced by CovidParser#mini.
    def exitMini(self, ctx:CovidParser.MiniContext):
        pass


    # Enter a parse tree produced by CovidParser#moment.
    def enterMoment(self, ctx:CovidParser.MomentContext):
        pass

    # Exit a parse tree produced by CovidParser#moment.
    def exitMoment(self, ctx:CovidParser.MomentContext):
        pass


    # Enter a parse tree produced by CovidParser#plot.
    def enterPlot(self, ctx:CovidParser.PlotContext):
        pass

    # Exit a parse tree produced by CovidParser#plot.
    def exitPlot(self, ctx:CovidParser.PlotContext):
        pass


    # Enter a parse tree produced by CovidParser#histogram.
    def enterHistogram(self, ctx:CovidParser.HistogramContext):
        pass

    # Exit a parse tree produced by CovidParser#histogram.
    def exitHistogram(self, ctx:CovidParser.HistogramContext):
        pass


    # Enter a parse tree produced by CovidParser#correl.
    def enterCorrel(self, ctx:CovidParser.CorrelContext):
        pass

    # Exit a parse tree produced by CovidParser#correl.
    def exitCorrel(self, ctx:CovidParser.CorrelContext):
        pass



del CovidParser