package com.frontierrealms;

import com.mojang.logging.LogUtils;
import net.minecraftforge.fml.common.Mod;
import org.slf4j.Logger;

@Mod(FrontierRealms.MOD_ID)
public final class FrontierRealms {
    public static final String MOD_ID = "frontier_realms";
    private static final Logger LOGGER = LogUtils.getLogger();

    public FrontierRealms() {
        LOGGER.info("Frontier Realms pack companion loaded for Minecraft 1.20.1.");
    }
}
