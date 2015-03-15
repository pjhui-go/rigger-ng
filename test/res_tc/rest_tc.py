#coding=utf8
import  utls.tpl ,interface ,base.tc_tools
import  impl.rg_args

class rest_tc(base.tc_tools.rigger_tc):
    def asst_cmd(self,conf,cmd):
        impl.rg_run.run_cmd(cmd,conf)

    def test_rest(self) :
        conf = utls.rg_var.value_of("${HOME}/devspace/rigger-ng/test/res_tc/res_rest.yaml")
        mock = base.tc_tools.res_mock()
        with   mock :
            self.asst_cmd(conf,"conf -s rest -e dev")
        sed = """sed -r "s/.+:class\s+(\S+)\s+.+\/\/\@REST_RULE:\s+(.+)/\\2 : \\1/g" """
        expect = """grep --include "*.php" -i  -E "class .+ implements XService"  -R ${PRJ_ROOT}/test/data/   |  """  +  sed + " > ${PRJ_ROOT}/test/data/_rest_conf.idx "
        self.assertMacroEqual(expect, mock.cmds)
